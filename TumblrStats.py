import requests
from urllib.parse import quote


class TumblrStats:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.tumblr.com/v2/tagged"
   
    def get_tumblr_data(self, movie):
        encoded_tag = quote(movie.replace(" ", "").lower())
        url = f"{self.base_url}?tag={encoded_tag}&api_key={self.api_key}&limit=20"
        response = requests.get(url).json()
       
        if "response" not in response or not response["response"]:
            return 0
           
        posts = response["response"]
        note_counts = [post.get("note_count", 0) for post in posts if "note_count" in post]
        top_5_notes = sorted(note_counts, reverse=True)[:5]
        return sum(top_5_notes) / len(top_5_notes) if top_5_notes else 0
