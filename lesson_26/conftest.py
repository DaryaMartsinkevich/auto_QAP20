import pytest
import requests
from lesson_26.endpoints.create_obj import CreateObj
from lesson_26.payload.payload import valid_create_payload, invalid_create_payload


@pytest.fixture()
def new_object():
    new_obj = CreateObj()
    new_obj.new_obj(valid_create_payload)
    object_id = new_obj.get_data()["id"]
    yield new_obj
    requests.delete(url=f"https://api.restful-api.dev/objects/{object_id}")


@pytest.fixture(params=[
    (valid_create_payload, True),
    (invalid_create_payload, False)
])
def test_data(request):
    """Фикстура для параметризации тестов"""
    return request.param