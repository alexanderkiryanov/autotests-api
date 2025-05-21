import asyncio
import websockets


async def echo(ws):
    async for message in ws:
        print(f"Получено сообщение: {message}")
        response = f"Сервер получил: {message}"
        await ws.send(response)

        for _ in range(5):
            await ws.send(response)


async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost 8765")
    await server.wait_closed()

asyncio.run(main())