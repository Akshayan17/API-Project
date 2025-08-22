import pytest
from unittest.mock import patch
from TumblrStats import TumblrStats
@patch("TumblrStats.requests.get")
def test_average_uses_top_5(mock_get):
   
    mock_get.return_value.json.return_value = {
        "response": [
            {"note_count": 100},
            {"note_count": 90},
            {"note_count": 80},
            {"note_count": 70},
            {"note_count": 60}
        ]
    }
    ts = TumblrStats(api_key="fygLC61xlnwf6j2XxXlDFDv2yk4ykjU2UJsRM92sRQr32Xyrfo9")
    result = ts.get_tumblr_data("Titanic")
    assert result == 80.0  
