import requests
import json
from flask import request, Flask

# Constants for API key and URL
API_KEY = "e6ef05302emsh9c46dd59d7ac5d1p13a2d8jsneb37aae7d452"
API_URL = "https://api.rawg.io/api/genres?key=10c5b7e4c1de4ddb83fb19e736dd91d0"

# Mapping of game genres to their corresponding index in the results
GENRE_MAPPING = {
    'action': 0,
    'adventure': 1,
    'puzzle': 8,
    'racing': 12,
    'RPG': 3,
    'sport': 13,
    'strategy': 4,
}

app = Flask(__name__)

def looking_game():
    # Set headers for the API request
    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }
    # Make API request to get game genres
    response = requests.get(API_URL, headers=headers)
    formatted_response = json.loads(response.text)
    return formatted_response['results']

@app.route('/', methods=['GET', 'POST'])
def game_search():
    # Retrieve game genres information
    result = looking_game()
    # Get JSON input from the request
    input_information = request.json
    # Initialize the games list with placeholder names
    games_list = [{'name'
