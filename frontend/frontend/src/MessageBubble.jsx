import ReactMarkdown from 'react-markdown';

function MessageBubble({ sender, text }) {
  const isUser = sender === 'user';
  return (
    <div className={`message ${isUser ? 'user' : 'assistant'}`}>
      <div className="bubble">
        <ReactMarkdown>{text}</ReactMarkdown>
      </div>
    </div>
  );
}

export default MessageBubble;
