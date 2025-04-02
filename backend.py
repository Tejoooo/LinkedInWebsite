from flask import Flask, request, jsonify
import requests
from flask_cors import CORS 
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)
#get the api key from the join proxyurl 
API_KEY = os.getenv('PROXY_URL_LINKEDIN')
API_ENDPOINT = "https://nubela.co/proxycurl/api/v2/linkedin"
HEADERS = {'Authorization': 'Bearer ' + API_KEY}

@app.route('/fetch_linkedin', methods=['GET'])
def fetch_linkedin():
    linkedin_url = request.args.get('url')
    if not linkedin_url:
        return jsonify({"error": "Missing 'url' parameter"}), 400
    
    response = requests.get(API_ENDPOINT, params={'url': linkedin_url}, headers=HEADERS)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
