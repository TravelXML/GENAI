# Gen-AI-With-Deep-Seek-R1

Here’s a detailed **README.md** file for your GitHub repository (`GENAI`). It explains the purpose of the project, how to set it up, and how to execute the necessary commands in a way that even a layman can understand.

---

# GENAI - DeepSeek Code Companion 🧠

Welcome to **GENAI**, your AI-powered coding assistant! This project leverages the power of **Ollama** and **LangChain** to provide you with an intelligent coding companion that can help you debug, document, and design solutions for your code. Whether you're a beginner or an experienced developer, GENAI is here to make your coding journey smoother and more efficient.

---

## 🚀 Features

- **🐍 Python Expert**: Get expert-level assistance with Python programming.
- **🐞 Debugging Assistant**: Identify and fix bugs in your code with strategic print statements.
- **📝 Code Documentation**: Automatically generate clear and concise documentation for your code.
- **💡 Solution Design**: Receive well-thought-out solutions for your coding challenges.

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed on your system:

1. **Python 3.8 or higher**: Download and install Python from [python.org](https://www.python.org/).
2. **Git**: Download and install Git from [git-scm.com](https://git-scm.com/).
3. **Ollama**: Follow the installation instructions from the [Ollama GitHub repository](https://github.com/jmorganca/ollama).

---

## 🏁 Getting Started

### Step 1: Clone the Repository

1. Open your terminal or command prompt.
2. Run the following command to clone the repository:

   ```bash
   git clone https://github.com/TravelXML/GENAI.git
   ```

3. Navigate into the cloned repository:

   ```bash
   cd GENAI
   ```

---

### Step 2: Set Up a Virtual Environment (Optional but Recommended)

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

---

### Step 3: Install Dependencies

1. Install the required Python packages using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

---

### Step 4: Pull the Ollama Model

1. Ensure Ollama is running on your system.
2. Pull the required model (e.g., `deepseek-r1:1.5b`):

   ```bash
   ollama pull deepseek-r1:1.5b
   ```

---

### Step 5: Run the Application

1. Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to the provided URL (usually `http://localhost:8501`).

---

## 🖥️ Using the App

1. **Select a Model**: Use the sidebar to choose between available models (e.g., `deepseek-r1:1.5b` or `deepseek-r1:3b`).
2. **Ask Questions**: Type your coding questions or problems in the chat input box.
3. **Get Answers**: The AI will provide concise and accurate solutions, debugging tips, or documentation.

---

## 📂 Project Structure

```
GENAI/
├── app.py                  # Main application file
├── requirements.txt        # List of dependencies
├── README.md               # This file
└── .gitignore              # Files and directories to ignore in Git
```

---

## 🤝 Contributing

We welcome contributions! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with [Ollama](https://ollama.ai/) and [LangChain](https://python.langchain.com/).
- Inspired by the need for smarter coding tools.

---

### Commands to RUN...

```bash
# Clone the repository
git clone https://github.com/TravelXML/GENAI.git
cd GENAI

# Set up a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Pull the Ollama model
ollama pull deepseek-r1:1.5b

# See All Ollama  Model available on your local
ollama list

# Run the application
streamlit run app.py
```

---
Display:
Enjoy coding with **UltimateSystemDesign (USD)**! [USD](https://ultimatesystemsdesign.com/) 🚀
![image](https://github.com/user-attachments/assets/45be5f64-a6b5-4a8e-b491-8194f471a035)
