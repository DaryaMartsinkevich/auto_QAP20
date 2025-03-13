import requests


def test_api_cat():
    url_cat = "https://api.thecatapi.com/v1/images/search"
    random_cat = requests.get(url_cat)
    json = random_cat.json()


url_voites = "https://api.thecatapi.com/v1/votes"
api_key = 'live_uju77iNoOWP2BwmK4N2nKGUUi3yM6mjMCADnNJ9NQRjjrnJNkHpwoyoI7dD0wQqj'


def vote_cat(image_id, value=1):
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "image_id": image_id,
        "value": value
    }
    response = requests.post(url_voites, json=data, headers=headers)

    if response.status_code == 201:
        print("Голос успешно отправлен!")
    else:
        print("Ошибка:", response.status_code, response.text)


vote_cat('image_id')


response = requests.get("https://api.thecatapi.com/v1/favourites")
headers = {"x-api-key": api_key}
favoutites_id = response.json()["id"]
print(favoutites_id)

response_delete = requests.delete(f"https://api.thecatapi.com/v1/favourites/{favoutites_id}",headers=headers)
print(response_delete.status_code, response.json())