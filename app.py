import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    name = data.get('name')
    msg = data.get('message')

    if not name or not msg:
        return jsonify({"success": False, "message": "कृपया सभी फ़ील्ड्स भरें!"}), 400

    # मैसेज मिलने पर रिस्पॉन्स
    print(f"📩 नया मैसेज आया! Name: {name}, Msg: {msg}")
    return jsonify({"success": True, "message": f"धन्यवाद {name}! आपका संदेश मिल गया है।"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
