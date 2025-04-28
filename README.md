# Speak-Tutor
SpeakTutor 🎙️
SpeakTutor is a web-based app that helps users practice and improve their English pronunciation.
It records your voice, compares it with a given sentence, gives a pronunciation score, and provides spoken feedback!

🚀 Features
🎤 Record your speech directly from the browser

✍️ Get real-time transcription of your voice

📊 See a pronunciation similarity score

🔊 Listen to spoken feedback with a friendly voice

🌐 Stylish, animated UI built with Tailwind CSS

🛠️ Technologies Used
Frontend: HTML5, Tailwind CSS, JavaScript (MediaRecorder API, SpeechSynthesis)

Backend: Python Flask

Speech Recognition: Google Web Speech API via speech_recognition library

Audio Conversion: FFmpeg (webm ➔ wav)

Others: Difflib for text similarity checking

📦 Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/speaktutor.git
cd speaktutor
Install Python dependencies:

bash
Copy
Edit
pip install flask speechrecognition
Install FFmpeg (required):

Windows: Download FFmpeg

Mac/Linux:

bash
Copy
Edit
brew install ffmpeg
or

bash
Copy
Edit
sudo apt install ffmpeg
Run the Flask app:

bash
Copy
Edit
python app.py
Open your browser:

Visit http://127.0.0.1:5000/

📁 Project Structure
bash
Copy
Edit
/recordings          # Folder to save recorded audio files
/static/script.js    # JavaScript for frontend logic
/templates/index.html # Main webpage
app.py               # Flask backend
🎯 Future Improvements
Allow users to input custom sentences

Support multiple languages

Build mobile-friendly app

Use advanced AI models for pronunciation scoring

🧑‍💻 Author
Mohammed Jaseem

📄 License
This project is licensed under the MIT License.

