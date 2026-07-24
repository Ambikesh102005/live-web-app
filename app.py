import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({
        "status": "Online 🟢",
        "message": "आपकी वेबसाइट इंटरनेट पर सफलतापूर्वक लाइव है!"
    })

if __name__ == '__main__':
    # PORT एनवायरनमेंट वेरिएबल लाइव सर्वर के लिए ज़रूरी होता है
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
