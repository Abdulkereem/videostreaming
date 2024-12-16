

# Wowza Live Stream Flask Project

This project demonstrates how to integrate **Wowza Streaming Engine** with a **Flask** application to manage and display live streams in real-time. It uses **Server-Sent Events (SSE)** to provide live stream status updates and **Video.js** to display video content from Wowza streams on the frontend.

## Features
- **Live Stream Playback**: Embeds a live stream using Wowza's HLS playback URL.
- **Real-Time Stream Status**: Displays the status of live streams (e.g., Online/Offline) using SSE.
- **Dynamic Stream Updates**: Automatically updates the list of live streams and their statuses on the frontend.
- **TailwindCSS**: Styled with **TailwindCSS** for a responsive, modern user interface.
  
---

## Requirements

- **Python 3.8+**
- **Flask**: A lightweight WSGI web application framework.
- **Flask-SSE**: For handling Server-Sent Events.
- **Video.js**: For embedding and playing HLS streams in the browser.
- **Redis**: Required by **Flask-SSE** for event handling.
- **Wowza Streaming Engine**: Used for creating and managing live streams.

---

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/wowza-flask-stream.git
cd wowza-flask-stream
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

- **Flask**: `Flask` web framework.
- **Flask-SSE**: To support Server-Sent Events.
- **requests**: For making API requests to Wowza.

### 3. Install Redis:

This project uses **Redis** for SSE support. Make sure **Redis** is installed and running on your local machine.

```bash
# For Ubuntu
sudo apt install redis-server
```

Start Redis:

```bash
redis-server
```

### 4. Configuration:

Create a `config.py` file with your Wowza API credentials and the base URL:

```python
WOWZA_API_BASE_URL = "https://your-wowza-api-url"
WOWZA_ACCESS_KEY = "your-access-key"
WOWZA_API_KEY = "your-api-key"
```

Ensure you have valid API credentials from **Wowza Streaming Engine**.

---

## Running the Application

### 1. Start the Flask server:
```bash
python app.py
```

The Flask application will start running on `http://127.0.0.1:5000`.

### 2. Open the application in a browser:
Go to `http://127.0.0.1:5000` to view the live streams and interact with the stream manager.

---

## Project Structure

```
/wowza-flask-stream
├── app.py                # Flask application logic
├── config.py             # Configuration file for API keys and URLs
├── requirements.txt      # List of required Python packages
└── templates
    └── index.html        # HTML template for the frontend
└── static
    └── /css
    └── /js
```

- `app.py`: The core Flask application that handles routing, API communication with Wowza, and SSE updates.
- `templates/index.html`: The HTML template that renders the stream manager UI and displays the live stream.
- `config.py`: Stores your Wowza API configuration (base URL and API keys).
- `requirements.txt`: Lists the necessary Python packages for the project.

---

## Frontend

### Video.js Integration
The live stream is displayed using **Video.js**, an HTML5 video player. It supports HLS streaming from Wowza, allowing the video stream to be viewed in real-time. The video player is automatically updated with the correct stream URL when the user clicks "Watch Stream."

### TailwindCSS
The project uses **TailwindCSS** for utility-first CSS to build a responsive layout with minimal custom styling.

### SSE for Real-Time Updates
The app uses **Server-Sent Events (SSE)** to stream updates about live stream status. The frontend listens for updates and dynamically renders the current status of live streams (e.g., Online or Offline).

---

## Usage

### Managing Streams
- The app connects to the Wowza API to manage live streams.
- You can start or stop streams by sending a `POST` request to `/streams/start/<stream_id>` or `/streams/stop/<stream_id>` respectively.
  
### Displaying Streams
- The list of streams is automatically updated in real-time using SSE.
- When a stream is online, users can click "Watch Stream" to view it on the page.

---

## Troubleshooting

- **SSE Not Working**: Ensure Redis is installed and running correctly.
- **CORS Issues**: Make sure your Wowza server allows requests from the frontend's domain.
- **Stream Issues**: Verify that your Wowza stream URL is correct and that the stream is live.

---



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

