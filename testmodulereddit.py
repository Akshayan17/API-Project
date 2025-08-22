import pytest
from RedditStats import initialize_reddit_client, get_reddit_data

@pytest.fixture
def reddit_client():
    return initialize_reddit_client()

def test_get_reddit_data_values_swapped(reddit_client):
    upvotes, comments = get_reddit_data(reddit_client, "The Matrix")

    assert upvotes >= comments, "Upvotes should be greater than or equal to comments for a popular movie"

def test_get_reddit_data_types(reddit_client):
    upvotes, comments = get_reddit_data(reddit_client, "The Matrix")

    assert isinstance(upvotes, int)
    assert isinstance(comments, int)
