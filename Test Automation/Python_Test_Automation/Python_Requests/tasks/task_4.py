import requests

url = "https://jsonplaceholder.typicode.com/users"


def get_user():
    return requests.get(url)


def validate_user():
    response = get_user()
    assert response.status_code == 200
    body = response.json()
    assert len(body) > 3
    assert "Ervin Howell" in response.text
    assert "Ervin Howell" in get_names()


def get_names():
    body = get_user().json()
    names = []
    for i in range(len(body)):
        names.append(body[i]["name"])
    return names


validate_user()
