import pytest
import json
from RedditStats import initialize_reddit_client, get_reddit_data
from OMDbStats import get_imdb_data
from TumblrStats import TumblrStats

@pytest.fixture
def load_movie_stats():
    with open("movie_stats.txt", "r") as f:
        movie_stats = json.load(f)
    return movie_stats


def test_data_structure_and_types(load_movie_stats):
    """
    Test if the structure and data types are correct for each movie.
    """
    movie_stats = load_movie_stats
    required_keys = {"reddit", "imdb", "tumblr"}
    imdb_keys = {"rating", "reviews"}
    reddit_keys = {"upvotes", "comments"}
    tumblr_keys = {"avg_notes"}

    for movie, data in movie_stats.items():
        # Check for required keys
        assert required_keys.issubset(data.keys()), f"Movie '{movie}' is missing required keys."
        assert imdb_keys.issubset(data["imdb"].keys()), f"Movie '{movie}' is missing IMDb keys."
        assert reddit_keys.issubset(data["reddit"].keys()), f"Movie '{movie}' is missing Reddit keys."
        assert tumblr_keys.issubset(data["tumblr"].keys()), f"Movie '{movie}' is missing Tumblr keys."

        # Check data types
        assert isinstance(data["reddit"]["upvotes"], int), f"Upvotes for '{movie}' should be an integer."
        assert isinstance(data["reddit"]["comments"], int), f"Comments for '{movie}' should be an integer."
        assert isinstance(data["imdb"]["rating"], str), f"Rating for '{movie}' should be a string." 
        assert isinstance(data["imdb"]["reviews"], int), f"Reviews for '{movie}' should be an integer."
        assert isinstance(data["tumblr"]["avg_notes"], (int, float)), f"Tumblr notes for '{movie}' should be a number."


def test_sorting(load_movie_stats):
    """
    Test if the sorting operation in the main code works correctly.
    """
    movie_stats = load_movie_stats
    sorted_movies = sorted(
        movie_stats.keys(),
        key=lambda movie: float(movie_stats[movie]["imdb"]["rating"]) 
        if movie_stats[movie]["imdb"]["rating"] not in ("N/A", "", None) else 0.0
    )
    
    ratings = [
        float(movie_stats[movie]["imdb"]["rating"])
        if movie_stats[movie]["imdb"]["rating"] not in ("N/A", "", None) else 0.0
        for movie in sorted_movies
    ]

    assert ratings == sorted(ratings), "The sorting operation failed."
