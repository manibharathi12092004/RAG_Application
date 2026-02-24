import React from 'react';
import ChatWindow from './ChatWindow';
import './index.css';

function App() {
  return (
    <div className="app-container">
      <header>
        PolicyMind AI
      </header>
      <main>
        <ChatWindow />
      </main>
    </div>
  );
}

export default App;
