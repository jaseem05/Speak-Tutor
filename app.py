from flask import Flask, request, jsonify, render_template
import speech_recognition as sr
import os
import difflib
from datetime import datetime
import subprocess  # To call ffmpeg for conversion

app = Flask(__name__)

UPLOAD_FOLDER = 'recordings'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_similarity(user_text, expected_text):
    similarity = difflib.SequenceMatcher(None, user_text.lower(), expected_text.lower()).ratio()
    return round(similarity * 100, 2)

# Function to convert .webm to .wav using ffmpeg
def convert_webm_to_wav(webm_path, wav_path):
    try:
        subprocess.run(['ffmpeg', '-i', webm_path, '-ac', '1', '-ar', '16000', wav_path], check=True)
        print("Conversion successful!")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
        return False
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    audio = request.files['audio_data']
    expected = request.form['expected_text']

    filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".webm"  # Save as .webm first
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    audio.save(filepath)

    # Convert .webm to .wav for speech recognition
    wav_path = os.path.splitext(filepath)[0] + ".wav"
    if not convert_webm_to_wav(filepath, wav_path):
        return jsonify({'error': 'Audio conversion failed'})

    # Perform speech recognition
    recognizer = sr.Recognizer()
    text = ""
    score = 0  # Default to 0 if recognition fails

    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            score = get_similarity(text, expected)
        except sr.UnknownValueError:
            return jsonify({'error': 'Could not understand audio'})
        except sr.RequestError:
            return jsonify({'error': 'Speech recognition failed'})

    # Generate feedback
    if score >= 80:
        feedback = "Great job! Your pronunciation is very clear."
    elif score >= 50:
        feedback = "Not bad, but you can improve your pronunciation."
    else:
        feedback = "Try again, focus on the pronunciation of each word."

    return jsonify({
        'transcription': text,
        'expected': expected,
        'score': score,
        'feedback': feedback
    })

if __name__ == '__main__':
    app.run(debug=True)
    # Note: In production, set debug=False and use a proper WSGI server like Gunicorn or uWSGI
    # and a reverse proxy like Nginx.