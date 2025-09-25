from flask import Flask, send_from_directory, jsonify
import os
from dotenv import load_dotenv

# Load environment variables from .env. By default load_dotenv does NOT override
# existing environment variables. For local development we can force .env to
# take precedence by passing override=True. Be careful with this in prod as
# it will overwrite any real environment variables.
load_dotenv(override=True)

# serve built files from frontend/dist
app = Flask(__name__, static_folder="frontend/dist", static_url_path="")

@app.route('/api/hello')
def hello():
    name = os.getenv("NAME", "GitHub Copilot")
    print(f"Environment variable NAME: {name}")
    return jsonify(message=f"{name}, hello world")

# Serve static files and index.html for client-side routing
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def static_proxy(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)