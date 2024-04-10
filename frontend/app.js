document.getElementById('start-recording').addEventListener('click', () => {
    startSpeechRecognition();
});

document.getElementById('connect-websocket').addEventListener('click', () => {
    connectWebSocket();
});

function displayTranscription(text) {
    const container = document.getElementById('transcriptions');
    const transcriptionElement = document.createElement('div');
    transcriptionElement.textContent = text;
    container.appendChild(transcriptionElement);
}

function connectWebSocket() {
    const ws = new WebSocket('ws://localhost:8000/ws');
    ws.onmessage = function(event) {
        displayTranscription(event.data);
    };
    ws.onerror = function(event) {
        console.error('WebSocket error:', event);
    };
    ws.onopen = function(event) {
        console.log('WebSocket connection established');
    };
    ws.onclose = function(event) {
        console.log('WebSocket connection closed');
    };
}

function startSpeechRecognition() {
    // Check for SpeechRecognition API support
    window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!window.SpeechRecognition) {
        alert("Your browser doesn't support the Web Speech API. Please use Google Chrome or another supported browser.");
        return;
    }

    // Initialize speech recognition
    const recognition = new window.SpeechRecognition();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    recognition.start();

    recognition.onresult = function(event) {
        const transcription = event.results[0][0].transcript;
        displayTranscription(transcription);
    };

    recognition.onerror = function(event) {
        console.error('Speech Recognition Error:', event.error);
    };

    recognition.onend = function() {
        // Automatically restart the recognition if stopped
        recognition.start();
    };
}
