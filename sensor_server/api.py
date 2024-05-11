from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

archive = open("D:\\sensor_server\\archive.json", "a")

latest = dict()

@app.post('/api/post_data')
def add_record():
    data = request.get_json()
    if data is None:
        return "", 400

    global latest
    latest = data
    archive.write(datetime.now().isoformat() + " " + json.dumps(data) + "\n")
    archive.flush()
    return "", 200

@app.get('/api/data')
def get_record():
    return jsonify(latest)

if __name__ == '__main__':
    app.run()

