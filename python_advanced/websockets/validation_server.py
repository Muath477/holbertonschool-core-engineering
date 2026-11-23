#!/usr/bin/env python3
import asyncio

import websockets
from websockets.exceptions import ConnectionClosed

HOST = "127.0.0.1"
PORT = 8765


def validate(message):
    if len(message.strip()) == 0:
        return "ERR:EMPTY"
    return "OK:" + message


async def connection_handler(websocket):
    try:
        async for message in websocket:
            await websocket.send(validate(message))
    except ConnectionClosed:
        pass


async def main():
    async with websockets.serve(connection_handler, HOST, PORT):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
