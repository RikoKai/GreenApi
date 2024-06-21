from flask import Flask, request, jsonify, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/getSettings', methods=['POST'])
def get_settings():
    data = request.json
    id_instance = data['idInstance']
    api_token_instance = data['apiTokenInstance']
    url = f"https://api.green-api.com/waInstance{id_instance}/getSettings/{api_token_instance}"
    response = requests.get(url)
    return jsonify(response.json())

@app.route('/api/getStateInstance', methods=['POST'])
def get_state_instance():
    data = request.json
    id_instance = data['idInstance']
    api_token_instance = data['apiTokenInstance']
    url = f"https://api.green-api.com/waInstance{id_instance}/getStateInstance/{api_token_instance}"
    response = requests.get(url)
    return jsonify(response.json())

@app.route('/api/sendMessage', methods=['POST'])
def send_message():
    data = request.json
    id_instance = data['idInstance']
    api_token_instance = data['apiTokenInstance']
    phone_number = data['phoneNumber']
    message = data['message']
    url = f"https://api.green-api.com/waInstance{id_instance}/sendMessage/{api_token_instance}"
    payload = {
        "chatId": f"{phone_number}@c.us",
        "message": message
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return jsonify(response.json())

@app.route('/api/sendFileByUrl', methods=['POST'])
def send_file_by_url():
    data = request.json
    id_instance = data['idInstance']
    api_token_instance = data['apiTokenInstance']
    phone_number = data['phoneNumber']
    file_url = data['fileUrl']
    url = f"https://api.green-api.com/waInstance{id_instance}/sendFileByUrl/{api_token_instance}"
    payload = {
        "chatId": f"{phone_number}@c.us",
        "urlFile": file_url
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
