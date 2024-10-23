from flask import Flask, request, jsonify, render_template
import SparkApi

app = Flask(__name__)

appid = "92b4865f"
api_secret = "M2ZjZDg0OTBjMTE2NTU3NjljYjIzZWNm"
api_key = "d2f69b2a76b462e3222349a91b3bb7d1"
domain = "generalv3.5"
Spark_url = "wss://spark-api.xf-yun.com/v3.5/chat"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data['message']
    max_tokens = data.get('max_tokens', 4096)
    top_k = data.get('top_k', 4)
    temperature = data.get('temperature', 0.5)

    text = [
        {"role": "user", "content": user_message}
    ]

    SparkApi.answer = ""
    SparkApi.main(appid, api_key, api_secret, Spark_url, domain, text, max_tokens, top_k, temperature)

    return jsonify({"response": SparkApi.answer})

if __name__ == '__main__':
    app.run(debug=True)