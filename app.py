from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Backend Running Changes-1-2-3-4"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)