import React, { useState, useRef, useEffect } from 'react';
import MessageBubble from './MessageBubble';
import InputBox from './InputBox';
import axios from 'axios';

const USER_ID = 1;

function ChatWindow() {
  const [messages, setMessages] = useState([
    { sender: 'assistant', text: 'Hello! How can I help you today?' }
  ]);
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef(null);

  useEffect(() => {
    if (chatEndRef.current) {
      chatEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages, loading]);

  const handleSend = async (userMessage) => {
    if (!userMessage.trim()) return;
    setMessages(prev => [...prev, { sender: 'user', text: userMessage }]);
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8000/api/chat/', {
        user_id: USER_ID,
        question: userMessage
      });
      setMessages(prev => [
        ...prev,
        { sender: 'assistant', text: response.data.answer }
      ]);
    } catch (error) {
      setMessages(prev => [
        ...prev,
        { sender: 'assistant', text: 'Sorry, something went wrong.' }
      ]);
    }
    setLoading(false);
  };

  return (
    <div className="chat-window">
      <div className="chat-history">
        {messages.map((msg, idx) => (
          <MessageBubble key={idx} sender={msg.sender} text={msg.text} />
        ))}
        {loading && (
          <MessageBubble sender="assistant" text={<span className="typing-indicator">Assistant is typing...</span>} />
        )}
        <div ref={chatEndRef} />
      </div>
      <InputBox onSend={handleSend} loading={loading} />
    </div>
  );
}

export default ChatWindow;
