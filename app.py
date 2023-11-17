from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
@app.route('/search', methods=['GET'])
def search_images():
    query = request.args.get('query', '')
    results = get_unsplash_images(query)
    return jsonify(results)

def get_unsplash_images(query):
    unsplash_access_key = 'unsplash_access_key'
    unsplash_api_url = 'https://api.unsplash.com/search/photos'

    headers = {
        'Accept-Version': 'v1',
        'Authorization': f'Client-ID {unsplash_access_key}'
    }

    params = {
        'query': query,
        'per_page': 5  # You can adjust this based on your needs
    }

    response = requests.get(unsplash_api_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return [{'url': photo['urls']['regular']} for photo in data['results']]
    else:
        return []

if __name__ == '__main__':
    app.run(debug=True)