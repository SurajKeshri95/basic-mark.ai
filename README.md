# basic-mark.ai

Mark AI is a beginner-friendly AI Voice Assistant built using Python. It can listen to voice commands, understand them, and perform basic tasks like searching information, opening websites, telling the time, speaking responses, and more. This project demonstrates the core principles of speech recognition, text-to-speech, and command automation.

🚀 Key Features
🎤 Voice Input Recognition using your microphone

🗣️ Text-to-Speech (TTS) output using a human-like voice

🌐 Internet Search – Opens Google, YouTube, Wikipedia, and more

🕒 Tells Current Time & Date

📁 Opens Common Applications or Files

🔁 Custom Command Handling – Add your own functions easily

💬 Conversational Prompts with basic AI responses

🧠 Technologies & Libraries Used
Python 3.x

speech_recognition – for converting speech to text

pyttsx3 – for text-to-speech output

wikipedia – to fetch information from Wikipedia

webbrowser – to open URLs in the browser

datetime – to tell time and date

os – for executing local system commands

📂 Project Structure
bash
Copy
Edit
mark-ai-voice-assistant/
├── mark.py              # Main Python script
├── requirements.txt        # List of required Python packages
└── README.md               # Project description
⚙️ How to Set Up & Run
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/surajkeshri95/mark-ai-voice-assistant.git
cd mark-ai-voice-assistant
2. Install the Required Libraries
Make sure Python is installed, then run:

bash
Copy
Edit
pip install -r requirements.txt
3. Run the Assistant
bash
Copy
Edit
python mark.py
Speak your commands like:

"What is the time?"

"Open YouTube"

"Search Python on Wikipedia"

"Who is Elon Musk?"

💻 Sample Commands & Responses
User Says	Mark AI Does
"What’s the time?"	Tells the current system time
"Search for Python"	Searches Python on Google
"Who is Albert Einstein?"	Reads a short Wikipedia summary aloud
"Open YouTube"	Launches youtube.com in your default browser

🛠️ Customization Ideas
Add support for sending emails

Integrate with ChatGPT or GPT APIs for smart answers

Add wake word detection (like "Hey Mark")

Control smart devices (IoT)

Add GUI using Tkinter or PyQt

📸 Preview
(Optional: Insert a screenshot or video of the assistant in action)

📌 Limitations
Requires internet for Wikipedia and Google search

Accuracy may depend on microphone quality and noise

Works best with clear, slow voice input

📜 License
This project is licensed under the MIT License.

🙋‍♂️ Acknowledgements
Special thanks to the open-source Python community and contributors of speech_recognition, pyttsx3, and wikipedia libraries.

