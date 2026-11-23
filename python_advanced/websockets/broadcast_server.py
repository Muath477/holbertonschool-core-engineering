#!/usr/bin/env python3
import asyncio

import websockets
from websockets.exceptions import ConnectionClosed

HOST = "127.0.0.1"
PORT = 8765

connected_clients = set()


async def broadcast(message):
    for client in list(connected_clients):
        try:
            await client.send(message)
        except ConnectionClosed:
            connected_clients.discard(client)


async def connection_handler(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await broadcast("B:" + message)
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    async with websockets.serve(connection_handler, HOST, PORT):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
