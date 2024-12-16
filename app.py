from flask import Flask, render_template, jsonify, request, Response
import requests
from flask_sse import sse
from config import WOWZA_API_BASE_URL, WOWZA_ACCESS_KEY, WOWZA_API_KEY
import time

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"  # Redis is required for SSE
app.register_blueprint(sse, url_prefix='/stream-updates')

# Headers for Wowza API
HEADERS = {
    "wsc-api-key": WOWZA_API_KEY,
    "wsc-access-key": WOWZA_ACCESS_KEY,
    "Content-Type": "application/json"
}

# Home route
@app.route("/")
def index():
    return render_template("index.html")

# SSE route for stream updates
@app.route("/sse-streams")
def sse_streams():
    def generate_updates():
        while True:
            try:
                # Fetch live streams from Wowza
                url = f"{WOWZA_API_BASE_URL}/live_streams"
                response = requests.get(url, headers=HEADERS)
                if response.status_code == 200:
                    streams = response.json().get("live_streams", [])
                    yield f"data: {streams}\n\n"
                else:
                    yield f"data: {response.text}\n\n"
            except Exception as e:
                yield f"data: {str(e)}\n\n"
            time.sleep(5)  # Update every 5 seconds

    return Response(generate_updates(), content_type="text/event-stream")

# Start a live stream
@app.route("/streams/start/<stream_id>", methods=["POST"])
def start_stream(stream_id):
    url = f"{WOWZA_API_BASE_URL}/live_streams/{stream_id}/start"
    response = requests.put(url, headers=HEADERS)
    if response.status_code == 200:
        return jsonify({"message": "Stream started successfully"})
    else:
        return jsonify({"error": "Failed to start stream"}), response.status_code

# Stop a live stream
@app.route("/streams/stop/<stream_id>", methods=["POST"])
def stop_stream(stream_id):
    url = f"{WOWZA_API_BASE_URL}/live_streams/{stream_id}/stop"
    response = requests.put(url, headers=HEADERS)
    if response.status_code == 200:
        return jsonify({"message": "Stream stopped successfully"})
    else:
        return jsonify({"error": "Failed to stop stream"}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)
