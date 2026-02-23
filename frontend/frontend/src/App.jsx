import React from 'react';
import ChatWindow from './components/ChatWindow';
import './styles/chat.css';

function App() {
  return (
    <div className="chat-app-container">
      <header className="chat-header">
        SaaS Support Assistant
      </header>
      <ChatWindow />
    </div>
  );
}

export default App;
