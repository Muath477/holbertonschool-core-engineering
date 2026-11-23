const SOCKET_URL = 'ws://localhost:8000/ws';

const statusLabel = document.getElementById('status');
const messageList = document.getElementById('messages');
const form = document.getElementById('message-form');
const input = document.getElementById('message-input');
const sendButton = form.querySelector('button');

const socket = new WebSocket(SOCKET_URL);

function setStatus (text, state) {
  statusLabel.textContent = text;
  statusLabel.dataset.state = state;
}

function currentTime () {
  return new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

function addMessage (text, direction) {
  const item = document.createElement('li');
  item.className = 'message ' + direction;

  const body = document.createElement('span');
  body.textContent = text;

  const time = document.createElement('time');
  time.textContent = currentTime();

  item.append(body, time);
  messageList.appendChild(item);
  messageList.scrollTop = messageList.scrollHeight;
}

socket.addEventListener('open', () => {
  setStatus('Connected', 'open');
  sendButton.disabled = false;
  input.focus();
});

socket.addEventListener('close', () => {
  setStatus('Connection lost', 'closed');
  sendButton.disabled = true;
});

socket.addEventListener('message', (event) => {
  addMessage(event.data, 'received');
});

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const text = input.value;
  if (text.trim() === '' || socket.readyState !== WebSocket.OPEN) {
    return;
  }
  socket.send(text);
  addMessage(text, 'sent');
  input.value = '';
  input.focus();
});
