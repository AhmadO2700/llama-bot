from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

MODEL_PATH = "./models/LLaMA-3.1-8B-Instruct-Q4_0.gguf"

@app.route("/completion", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    n_predict = data.get("n_predict", 256)

    try:
        result = subprocess.run(
            ["./llama.cpp/main", "-m", MODEL_PATH, "-p", prompt, "-n", str(n_predict)],
            capture_output=True, text=True
        )
        output = result.stdout.strip()
        return jsonify({"content": output})
    except Exception as e:
        return jsonify({"content": f"Error: {str(e)}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
