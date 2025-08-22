import requests
from urllib.parse import quote


# API configuration
API_KEY = "c78bb14c"
BASE_URL = "http://www.omdbapi.com/"


def get_imdb_data(movie):
    # Construct the URL for the API call, encoding the movie title.
    url = f"{BASE_URL}?apikey={API_KEY}&t={quote(movie)}"
   
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        # If an error occurs (e.g., network error), print an error message and return default values.
        print(f"Error: Unable to retrieve data from OMDb API: {e}. Using defaults for IMDb data.")
        return "0", 0


    # Check if the API indicates that the movie was not found.
    if data.get("Response", "False") == "False":
        print(f"Warning: Movie '{movie}' not found on OMDb. Using defaults for IMDb data.")
        return "0", 0
   
    # Retrieve the IMDb rating and votes from the response.
    rating = data.get("imdbRating", "0")
    votes = data.get("imdbVotes", "0")
   
    # Convert 'N/A' values to default "0".
    if rating == "N/A":
        rating = "0"
    if votes == "N/A":
        votes = "0"
   
    try:
        votes = int(votes.replace(',', ''))
    except ValueError:
        # If conversion fails, set votes to 0.
        votes = 0


    return rating, votes
