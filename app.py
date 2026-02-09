from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask! branch test"
def ai():
    return jsonify({
		"invoke_ai"":"predict next buy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
