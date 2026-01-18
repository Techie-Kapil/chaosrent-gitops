from flask import Flask
import os

app = Flask(__name__)

@app.get("/")
def hello():
    return {
        "service": "chaosrent-echo",
        "version": os.getenv("APP_VERSION", "dev"),
        "status": "ok"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

