import { useState } from 'react';
import MessageBubble from './MessageBubble';
import InputBox from './InputBox';

function ChatWindow() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async (text) => {
    if (!text.trim()) return;
    setMessages([...messages, { sender: 'user', text }]);
    setLoading(true);
    try {
      // Replace with your backend API call
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text })
      });
      const data = await response.json();
      setMessages((msgs) => [...msgs, { sender: 'ai', text: data.reply }]);
    } catch (e) {
      setMessages((msgs) => [...msgs, { sender: 'ai', text: 'Sorry, something went wrong.' }]);
    }
    setLoading(false);
  };

  return (
    <div className="w-full max-w-xl flex flex-col h-[80vh] bg-white rounded-lg shadow-lg overflow-hidden">
      <div className="flex-1 overflow-y-auto p-4 space-y-2">
        {messages.map((msg, idx) => (
          <MessageBubble key={idx} sender={msg.sender} text={msg.text} />
        ))}
        {loading && (
          <div className="flex items-center space-x-2">
            <span className="animate-spin h-5 w-5 border-4 border-blue-400 border-t-transparent rounded-full"></span>
            <span className="text-gray-500">AI is typing...</span>
          </div>
        )}
      </div>
      <div className="border-t p-3 bg-gray-50">
        <InputBox onSend={sendMessage} loading={loading} />
      </div>
    </div>
  );
}

export default ChatWindow;
