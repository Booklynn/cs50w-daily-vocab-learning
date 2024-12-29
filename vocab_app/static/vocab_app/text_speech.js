function speakWord(word) {
    if ('speechSynthesis' in window) {
        const utterance = new SpeechSynthesisUtterance(word);
        utterance.lang = 'en-US';
        utterance.pitch = 1;
        utterance.rate = 0.4;
        window.speechSynthesis.speak(utterance);
    } else {
        alert("Text-to-Speech is not supported in your browser.");
    }
}
