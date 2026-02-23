import React from 'react';

function MessageBubble({ sender, text }) {
  return (
    <div className={
      sender === 'user'
        ? 'message-bubble user-bubble'
        : 'message-bubble assistant-bubble'
    }>
      <span>{text}</span>
    </div>
  );
}

export default MessageBubble;
