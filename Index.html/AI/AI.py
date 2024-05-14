from flask import Flask, request, jsonify

import requests
import json

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    url = "https://backend.aichattings.com/api/v2/chatgpt/talk"

    headers = {
        "Sec-Ch-Ua": "\"Chromium\";v=\"123\", \"Not:A-Brand\";v=\"8\"",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "*/*",
        "Origin": "https://frontend.aichattings.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://frontend.aichattings.com/?v=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=4, i"
    }

    msg = request.form.get('msg')

    data = {
        "msg": msg,
        "model": "gpt3",
        "locale": "en",
        "ep_user_id": 12910
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    return jsonify({"response": response.text})

@app.route('/')
def index():
    return """
    <form action="/chat" method="post">
        <label for="msg">Enter your message:</label><br>
        <input type="text" id="msg" name="msg"><br>
        <input type="submit" value="Submit">
    </form>
    """

if __name__ == '__main__':
    app.run(debug=True)
