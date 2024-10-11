import pytest

from app.util import jsonify

def test_jsonify():
    result = jsonify(
        state = {"data" : "test"},
        metadata = {"metadata" : "test"},
        headers = {"x-api-Header" : "test"},
        status = 200
    )
    assert type(result) is tuple
    assert result[0] == {"data" : "test", "metadata" : "test"}
    assert result[1] == 200
    assert result[2] == {"x-api-Header" : "test"}
