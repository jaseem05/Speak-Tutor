const recordBtn = document.getElementById('record');
const resultText = document.getElementById('result');
const scoreText = document.getElementById('score');
const feedbackText = document.getElementById('feedback');
const expected = document.getElementById('expected').innerText;

let mediaRecorder;
let audioChunks = [];

recordBtn.onclick = async () => {
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  mediaRecorder = new MediaRecorder(stream);
  audioChunks = [];

  mediaRecorder.ondataavailable = e => audioChunks.push(e.data);

  mediaRecorder.onstop = async () => {
    const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
    const formData = new FormData();
    formData.append('audio_data', audioBlob, 'speech.wav');
    formData.append('expected_text', expected);

    const res = await fetch('/upload', { method: 'POST', body: formData });
    const data = await res.json();

    if (data.error) {
      resultText.textContent = data.error;
      scoreText.textContent = "N/A";
      feedbackText.textContent = "";
    } else {
      resultText.textContent = data.transcription;
      scoreText.textContent = data.score + "%";
      feedbackText.textContent = data.feedback;

      // Speak feedback
      const utterance = new SpeechSynthesisUtterance(data.feedback);
      speechSynthesis.speak(utterance);
    }
  };

  mediaRecorder.start();
  recordBtn.textContent = "⏹ Stop";

  setTimeout(() => {
    mediaRecorder.stop();
    recordBtn.textContent = "🎤 Start Recording";
},3000);
};