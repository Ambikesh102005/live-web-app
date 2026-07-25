import os
import logging
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS सपोर्ट इनेबल किया गया

# Logging सेटअप
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"success": False, "message": "Invalid JSON payload"}), 400

        name = data.get('name', '').strip()
        msg = data.get('message', '').strip()

        # Input Validation (Copilot Recommendation)
        if not name or not msg:
            return jsonify({"success": False, "message": "कृपया सभी फ़ील्ड्स भरें!"}), 400
        
        if len(name) > 100 or len(msg) > 1000:
            return jsonify({"success": False, "message": "इनपुट सीमा से अधिक है!"}), 400

        logging.info(f"📩 नया मैसेज आया! Name: {name}")
        return jsonify({"success": True, "message": f"धन्यवाद {name}! आपका संदेश मिल गया है।"})

    except Exception as e:
        logging.error(f"Error processing contact form: {str(e)}")
        return jsonify({"success": False, "message": "सर्वर में कोई गड़बड़ी हुई!"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    # Production Environment Aware Debug Mode
    is_dev = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=is_dev)
