#!/usr/bin/env python3
import asyncio
import os

import websockets

DEFAULT_URI = "ws://localhost:8765"
DEFAULT_MESSAGE = "Hello WebSocket"
PLATFORM_MESSAGE = "demo"


async def connect_and_send(uri: str, text: str) -> str:
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        return await websocket.recv()


async def main():
    platform_uri = os.environ.get("WS_URI")
    if platform_uri:
        response = await connect_and_send(platform_uri, PLATFORM_MESSAGE)
    else:
        response = await connect_and_send(DEFAULT_URI, DEFAULT_MESSAGE)
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
