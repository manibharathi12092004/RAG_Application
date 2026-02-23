import { useState } from 'react';

function InputBox({ onSend, loading }) {
  const [input, setInput] = useState('');

  const handleSend = () => {
    if (!input.trim() || loading) return;
    onSend(input);
    setInput('');
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') handleSend();
  };

  return (
    <div className="flex items-center gap-2">
      <input
        type="text"
        className="flex-1 px-3 py-2 rounded border border-gray-300 focus:outline-none focus:ring focus:border-blue-400"
        placeholder="Type your message..."
        value={input}
        onChange={e => setInput(e.target.value)}
        onKeyDown={handleKeyDown}
        disabled={loading}
      />
      <button
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 disabled:opacity-50"
        onClick={handleSend}
        disabled={loading || !input.trim()}
      >
        Send
      </button>
    </div>
  );
}

export default InputBox;
