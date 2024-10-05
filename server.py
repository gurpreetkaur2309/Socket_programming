import asyncio
import websockets

async def handler(websocket, path):
    print("A new client connected")
    await websocket.send("Welcome new client!")

    async for message in websocket:
        print(f"Received message: {message}")
        await websocket.send(f"Hello Client! You said: {message}")

    print("Client has disconnected")

start_server = websockets.serve(handler, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
