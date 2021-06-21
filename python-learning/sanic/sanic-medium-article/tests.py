# import json
# from humps import camelize
from main import app


def test_get_request():
    """test_get_request function tests get requests for middleware
    The purpose of this test is to check if hte middleware would work
    if the request has no payload in case of "GET" requests.
    However the response should be camelized.
    """
    request, response = app.test_client.get("/")
    assert response.status == 200
    assert response.json == {"isCamelcase": True, "message": "Hello_world"}
