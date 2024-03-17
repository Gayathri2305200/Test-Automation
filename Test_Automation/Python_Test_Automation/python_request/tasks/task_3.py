import requests

url = "https://petstore.swagger.io/v2/pet/"
# header={'content-type': 'application/json'}
request_body = {"id": 12345, "category": {"id": 1, "name": "dog"}, "name": "snoopie", "photoUrls": ["string"],
                "tags": [{"id": 0, "name": "string"}], "status": "pending"}


def post_pet(url, request_body):
    r = requests.post(url, json=request_body)
    assert r.status_code == 200


def get_pet(url):
    r1 = requests.get(url + "12345")
    body = r1.json()
    assert r1.status_code == 200 and r1.headers['content-type'] == 'application/json'
    assert body["category"]["name"] == "dog"
    assert body["name"] == "snoopie"
    assert body["status"] == "pending"


post_pet(url, request_body)
get_pet(url)
