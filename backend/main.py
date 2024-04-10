from fastapi import FastAPI, WebSocket
import uvicorn
import threading
from audio_processor import start_audio_processing_thread

app = FastAPI() 

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    # Start the audio processing in a separate thread
    thread = threading.Thread(target=start_audio_processing_thread, args=(websocket,))
    thread.start()
    
    # Keep the connection open by listening for a message to close it
    try:
        while True:
            data = await websocket.receive_text()
            if data == "close":
                print("Closing the WebSocket connection on client's request.")
                break
    except Exception as e:
        print(f"WebSocket connection closed with exception: {e}")
    finally:
        # Clean up and close the thread and WebSocket connection here if necessary
        print("Cleaning up resources...")
        # thread.join() # Caution: Only use if you're sure it won't block. You might need to signal the thread to finish instead.

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
