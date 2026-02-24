import { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import MessageBubble from './MessageBubble';
import InputBox from './InputBox';

function ChatWindow() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef(null);

  const scrollToBottom = () => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, loading]);

  const sendMessage = async (text) => {
    if (!text.trim()) return;

    // Add user message to state
    const userMessage = { sender: 'user', text };
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/chat/', {
        user_id: 1,
        question: text
      });

      // Assuming the response data structure has the AI's reply
      // Update this based on the actual backend response format if different
      const aiReply = response.data.answer || response.data.response || response.data.reply;

      setMessages((prev) => [...prev, { sender: 'assistant', text: aiReply }]);
    } catch (e) {
      setMessages((prev) => [...prev, { sender: 'assistant', text: '⚠️ PolicyMind AI: Sorry, I am having trouble connecting to the server. Please check if the backend is running.' }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-window">
        {messages.map((msg, idx) => (
          <MessageBubble key={idx} sender={msg.sender} text={msg.text} />
        ))}

        {loading && (
          <div className="message assistant">
            <div className="bubble thinking">
              PolicyMind AI is thinking
              <span className="dot-flashing"></span>
            </div>
          </div>
        )}

        <div ref={chatEndRef} />
      </div>

      <InputBox onSend={sendMessage} loading={loading} />
    </div>
  );
}

export default ChatWindow;
