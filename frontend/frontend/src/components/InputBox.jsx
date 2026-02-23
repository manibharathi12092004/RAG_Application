import React, { useState } from 'react';

function InputBox({ onSend, loading }) {
  const [input, setInput] = useState('');

  const handleChange = (e) => {
    setInput(e.target.value);
  };

  const handleSend = () => {
    if (!input.trim() || loading) return;
    onSend(input);
    setInput('');
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      handleSend();
    }
  };

  return (
    <div className="input-box-container">
      <input
        className="chat-input"
        type="text"
        placeholder="Type your message..."
        value={input}
        onChange={handleChange}
        onKeyDown={handleKeyDown}
        disabled={loading}
        autoFocus
      />
      <button
        className="send-button"
        onClick={handleSend}
        disabled={loading || !input.trim()}
      >
        Send
      </button>
    </div>
  );
}

export default InputBox;
