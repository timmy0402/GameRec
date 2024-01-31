import requests
import json
from flask import request, Flask

def looking_game():
    url = "https://api.rawg.io/api/genres?key=10c5b7e4c1de4ddb83fb19e736dd91d0"
    headers = {
    'x-rapidapi-key': "e6ef05302emsh9c46dd59d7ac5d1p13a2d8jsneb37aae7d452",
    'x-rapidapi-host': "rawg-video-games-database.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    formatted_response = json.loads((response.text))
    formatted_response = formatted_response['results']
    print(formatted_response)
    return formatted_response
looking_game()
app = Flask(__name__)
@app.route('/',methods=['GET', 'POST'])
def game_search():
    result = looking_game()
    print("hello world")
    input_information = request.json
    games_list = [{'name':'g1'},{'name':'g2'},{'name':"g3"}]
    
    if input_information['game'] == 'action':
        games = result[0]['games']
        for i in range(3):
            games_list[i]['name'] = games[i]['name']
    elif input_information['game'] == 'adventure':
        games = result[1]['games']
        for i in range(3):
            games_list[i]['name'] = games[i]['name']
    elif input_information['game'] == 'puzzle':
        games = result[8]['games']
        for i in range(3):
            games_list[i]['name'] = games[i]['name'] 
    elif input_information['game'] == 'racing':
        games = result[12]['games']
        for i in range(3):
            games_list[i]['name'] = games[i]['name']
    elif input_information['game'] == 'RPG':
        games = result[3]['games']
        for i in range(3):
            games_list[i]['name'] = games[i]['name'] 
    elif input_information['game'] == 'racing':
        games = result[12]['games']
        for i in range(3):
            games_list[i]['name'] = games[i]['name']
    elif input_information['game'] == 'sport':
        games = result[13]['games']
        for i in range(3):
            games_list[i]['name'] = games[i]['name'] 
    elif input_information['game'] == 'strategry':
        games = result[4]['games']
        for i in range(3):
            games_list[i]['name'] = games[i]['name'] 
    
    return {"response_message":games_list}

if __name__ == "__main__":
    app.run()
