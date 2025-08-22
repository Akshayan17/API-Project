import requests
from OMDbStats import get_imdb_data


# Test case: API (IMDb site) is down.
def test_api_down():
    movie = "Inception"
   
    # Fake API response by raising an exception to simulate site down.
    def fake_get(url):
        raise requests.exceptions.RequestException("API is down")
   
    requests.get = fake_get


    try:
        rating, votes = get_imdb_data(movie)
    except Exception as e:
        print("Test API Down:")
        print("Bug found: Exception raised when API is down:", e)
        # This indicates a bug because the function should handle the exception gracefully.
        assert False, "API down case not handled gracefully"
    else:
        print("Test API Down:")
        print("Expected rating: 0, Got:", rating)
        print("Expected votes: 0, Got:", votes)
        assert rating == "0", "Expected rating to be 0 when API is down"
        assert votes == 0, "Expected votes to be 0 when API is down"