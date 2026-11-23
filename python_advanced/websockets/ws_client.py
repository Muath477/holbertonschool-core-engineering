#!/usr/bin/env python3
import asyncio
import os

import websockets

DEFAULT_URI = "ws://localhost:8765"


async def connect_and_send(uri: str, text: str) -> str:
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        return await websocket.recv()


async def main():
    uri = os.environ.get("WS_URI", DEFAULT_URI)
    response = await connect_and_send(uri, "demo")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
