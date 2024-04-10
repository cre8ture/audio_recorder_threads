# Real-Time Audio Transcription Application

This application captures your computer's audio output, transcribes it in real-time using a speech recognition service, and streams the transcriptions back to a web client through a WebSocket connection. The project is divided into two main parts: a FastAPI backend that handles audio transcription and WebSocket communication, and a simple frontend to display the transcriptions.

## Requirements

- Python 3.8 or newer
- Pip for Python package management
- A modern web browser that supports WebSockets

## Installation

First, clone this repository to your local machine and navigate into the project directory:

```sh
git clone <repository-url>
cd <project-directory>
```

### Backend Setup

1. **Create and Activate a Python Virtual Environment** (Recommended):

   On Windows:
   ```sh
   python -m venv venv
   .\venv\Scripts\activate
   ```
   
   On macOS and Linux:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install Required Python Packages**:

   Install all the required packages using the `requirements.txt` file:
   ```sh
   pip install -r requirements.txt
   ```

3. **Running the FastAPI Server**:

   With all dependencies installed, start the FastAPI server using Uvicorn:
   ```sh
   uvicorn main:app --reload
   ```
   The `--reload` flag enables live reloading during development.

### Frontend Setup

The frontend is a simple HTML page that uses JavaScript to connect to the WebSocket and display transcriptions.

1. **Navigate to the Frontend Directory**:

   Assuming the frontend files are located in a directory named `frontend` within the project:
   ```sh
   cd frontend
   ```

2. **Start a Simple HTTP Server**:

   Start a Python HTTP server on port 4001:
   ```sh
   python -m http.server 4001
   ```
   You can use any available port by replacing `4001` with your desired port number.

3. **Accessing the Web Interface**:

   Open a web browser and navigate to `http://localhost:4001`. You should see the web interface of the real-time audio transcription application.


## Backend
Sure, here's how you can modify the "Backend Setup" section to include details about navigating into the backend directory before running Uvicorn:

```markdown
### Backend Setup

1. **Navigate to the Backend Directory**:

   Assuming the backend files are located in a directory named `backend` within the project:
   ```sh
   cd backend
   ```

2. **Create and Activate a Python Virtual Environment** (Recommended):

   On Windows:
   ```sh
   python -m venv venv
   .\venv\Scripts\activate
   ```

   On macOS and Linux:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Required Python Packages**:

   Install all the required packages using the `requirements.txt` file:
   ```sh
   pip install -r requirements.txt
   ```

4. **Running the FastAPI Server**:

   With all dependencies installed, start the FastAPI server using Uvicorn:
   ```sh
   uvicorn main:app --reload
   ```
   The `--reload` flag enables live reloading during development.
```


## Usage

With both the FastAPI server running and the frontend accessible via a web browser, the application is ready for use. Here's how it works:

- The FastAPI backend captures your computer's audio output and uses speech recognition to transcribe it in real-time.
- Transcriptions are then sent to the frontend through a WebSocket connection.
- The frontend displays the transcriptions as they are received.

Please note, the actual capturing of system audio may require additional configuration depending on your operating system. This README assumes that the `main.py` in your FastAPI application and the necessary frontend files are properly set up as described in the instructions.

## Troubleshooting

- **Dependencies Not Installing**: Ensure you are using a compatible Python version and that your virtual environment is activated.
- **WebSocket Connection Issues**: Check that the FastAPI server is running and accessible. Ensure that the WebSocket URL in the frontend matches the URL and port where the FastAPI server is running.
- **Audio Capture Not Working**: Capturing system audio is highly dependent on the operating system and may require additional setup or permissions.

For more detailed troubleshooting, consult the documentation of the respective technologies used in this project.

