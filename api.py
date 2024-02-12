import requests
import json

with open('.secrets/creds.json') as f:
    creds = json.load(f)


url = f"https://api.themoviedb.org/3/movie/popular?api_key={creds['key']}" #Rest Api

movies_data = requests.get(url).json()


def beautify(data:list):
    return json.dumps(data, indent=4)

movies:list = movies_data["results"]

filtered_movies = []

def filter_movies(data:list, language:str, threshold:int):
    for movie in data:
        if movie["original_language"] == language and movie["vote_average"] > threshold:
            filtered_movies.append(movie)
    return filtered_movies
