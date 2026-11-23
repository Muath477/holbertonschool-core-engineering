# Real-time communication with WebSockets

WebSocket servers and clients in Python with the `websockets` library and
`async`/`await`, then the same echo logic as an ASGI app with Starlette and a
small chat page in the browser.

## Files

| File | Description |
| --- | --- |
| `echo_server.py` | Sends every message back to its sender |
| `ws_client.py` | `connect_and_send(uri, text)` sends one message and returns the reply; running it sends `Hello WebSocket` to `ws://localhost:8765` and prints the reply with no newline |
| `validation_server.py` | Replies `OK:<message>`, or `ERR:EMPTY` when the message is empty or only whitespace |
| `unicast_server.py` | Keeps track of clients and replies `U:<message>` only to the sender |
| `broadcast_server.py` | Sends `B:<message>` to every connected client and drops the ones that disconnected |
| `asgi_server.py` | Starlette app: `/` returns `<h1>WebSocket Echo</h1>` and `/ws` is a WebSocket echo |
| `index.html`, `styles.css`, `chat.js` | Browser chat that connects to `ws://localhost:8000/ws` |

The `websockets` servers listen on `127.0.0.1:8765`. When the `WS_URI` variable
is set, `ws_client.py` connects to that URI instead and sends `demo`.

## Usage

```
$ pip install websockets starlette uvicorn
$ python3 echo_server.py
$ python3 ws_client.py
Hello WebSocket
```

```
$ uvicorn asgi_server:app --host 0.0.0.0 --port 8000 --reload
```

With the ASGI server running, open `index.html` in a browser to chat. Each
message shows on the right when sent and on the left when the server's reply
comes back. The status line shows when the connection opens or is lost.
