from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/fetch-listings', methods=['GET'])
def fetch_equipment_listings():
    # Get rarity from request parameters, default to 'diamond' if not provided
    rarity = request.args.get('rarity', 'diamond')
    cardType = request.args.get('type', 'mlb_card')
    page = request.args.get('page', '1')
    # Construct the API request URL
    api_url = 'https://mlb25.theshow.com/apis/listings.json'
    params = {
        'type': cardType,
        'rarity': rarity,
        'sort': 'best_sell_price',
        'order': 'desc',
        'page': page
    }

    # Make the request to the external API
    response = requests.get(api_url, params=params)

    # Return the JSON response from the API to the frontend
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
