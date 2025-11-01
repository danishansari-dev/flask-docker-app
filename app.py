from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Flask CI/CD - AUTO DEPLOY v2.0! 🚀",
        "version": "2.0",
        "status": "running"

    })
    

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
