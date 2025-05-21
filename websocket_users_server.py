import asyncio
import websockets


async def echo(websocket: websockets.ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")

        for index in range(5):
            await websocket.send(f"{index + 1} Сообщение пользователя: {message}")

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    await server.wait_closed()

asyncio.run(main())