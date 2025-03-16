import requests
import jsonschema


schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "data": {
            "type": "object",
            "properties": {
                "year": {"type": "integer"},
                "price": {"type": "number"},
                "CPU model": {"type": "string"},
                "Hard disk size": {"type": "string"}
            },
            "required": ["year", "price", "CPU model", "Hard disk size"]
        }
    },
    "required": ["id", "name", "data"]
}


def create_obj():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1TB"
        }
    }
    response = requests.post("https://api.restful-api.dev/objects",
                             json=payload).json()
    assert response['name'] == payload['name'], '[post] Неверное имя'
    jsonschema.validate(instance=response, schema=schema)
    print(response)
    return response['id']


def get_obj():
    response = requests.get(f"https://api.restful-api.dev/objects/{create_obj()}").json()
    print(response)


if __name__ == '__main__':
    get_obj()