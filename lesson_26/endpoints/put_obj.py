import requests
from lesson_26.endpoints.base_endpoint import Endpoint


class PutObj(Endpoint):
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
            },
            "updatedAt": {"type": "string"}
        },
        "required": ["id", "name", "data", "updatedAt"]
    }

    def put_obj(self, update_create_payload, obj_id):
        self.response = requests.put(f"{self.url}/objects/{obj_id}", json=update_create_payload)
        self.response_json = self.response.json()

    def get_put_obj_id(self):
        return self.get_data()['id']

    def get_put_obj_name(self):
        return self.get_data()['name']

    def get_put_obj_data(self):
        return self.get_data()['data']