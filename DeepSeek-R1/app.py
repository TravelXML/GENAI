# Import necessary libraries
import streamlit as st  # Streamlit is used to create web apps
from langchain_ollama import ChatOllama  # ChatOllama is used to interact with the Ollama language model
from langchain_core.output_parsers import StrOutputParser  # Converts model output to a string

from langchain_core.prompts import (
    SystemMessagePromptTemplate,  # Template for system messages
    HumanMessagePromptTemplate,   # Template for user messages
    AIMessagePromptTemplate,      # Template for AI responses
    ChatPromptTemplate            # Combines all message templates
)

# Custom CSS styling for the app
st.markdown("""
<style>
    /* Set the background color and text color for the main app */
    .main {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    /* Style the sidebar background */
    .sidebar .sidebar-content {
        background-color: #2d2d2d;
    }
    /* Style the text input box */
    .stTextInput textarea {
        color: #ffffff !important;
    }
    
    /* Style the select box (dropdown) */
    .stSelectbox div[data-baseweb="select"] {
        color: white !important;
        background-color: #3d3d3d !important;
    }
    
    /* Style the dropdown arrow */
    .stSelectbox svg {
        fill: white !important;
    }
    
    /* Style the dropdown options */
    .stSelectbox option {
        background-color: #2d2d2d !important;
        color: white !important;
    }
    
    /* Style the dropdown menu items */
    div[role="listbox"] div {
        background-color: #2d2d2d !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)  # Allow HTML in Streamlit for custom styling

# Set the title and caption for the app
st.title("🧠 https://ultimatesystemsdesign.com // DeepSeek Code Companion")
st.caption("🚀 Your AI Pair Programmer with Debugging Superpowers")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    # Dropdown to select the model
    selected_model = st.selectbox(
        "Choose Model",
        ["deepseek-r1:1.5b", "deepseek-r1:3b"],  # Available models
        index=0  # Default selection
    )
    st.divider()  # Add a horizontal line
    st.markdown("### Model Capabilities")
    st.markdown("""
    - 🐍 Python Expert
    - 🐞 Debugging Assistant
    - 📝 Code Documentation
    - 💡 Solution Design
    """)
    st.divider()
    st.markdown("Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/)")  # Credits

# Initialize the chat engine with the selected model
llm_engine = ChatOllama(
    model=selected_model,  # Use the selected model
    base_url="http://localhost:11434",  # Ollama server URL
    temperature=0.3  # Controls randomness in responses (0 = deterministic, 1 = creative)
)

# Define the system prompt (instructions for the AI)
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an expert AI coding assistant. Provide concise, correct solutions "
    "with strategic print statements for debugging. Always respond in English."
)

# Manage session state to store chat history
if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"}]

# Create a container to display chat messages
chat_container = st.container()

# Display all chat messages in the container
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):  # Display message based on role (user or AI)
            st.markdown(message["content"])  # Render the message content

# Chat input for the user to type their question
user_query = st.chat_input("Type your coding question here...")

# Function to generate AI response
def generate_ai_response(prompt_chain):
    # Create a processing pipeline: prompt -> model -> output parser
    processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.invoke({})  # Invoke the pipeline and return the response

# Function to build the prompt chain (combines system, user, and AI messages)
def build_prompt_chain():
    prompt_sequence = [system_prompt]  # Start with the system prompt
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            # Add user messages to the prompt sequence
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            # Add AI responses to the prompt sequence
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
    return ChatPromptTemplate.from_messages(prompt_sequence)  # Combine all messages into a single prompt

# If the user submits a query
if user_query:
    # Add the user's query to the chat history
    st.session_state.message_log.append({"role": "user", "content": user_query})
    
    # Generate the AI's response
    with st.spinner("🧠 Processing..."):  # Show a loading spinner
        prompt_chain = build_prompt_chain()  # Build the prompt chain
        ai_response = generate_ai_response(prompt_chain)  # Get the AI's response
    
    # Add the AI's response to the chat history
    st.session_state.message_log.append({"role": "ai", "content": ai_response})
    
    # Rerun the app to update the chat display
    st.rerun()