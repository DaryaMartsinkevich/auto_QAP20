from lesson_26.endpoints.create_obj import CreateObj
from lesson_26.endpoints.base_endpoint import Endpoint
from lesson_26.payload.payload import valid_create_payload


def test_create_obj():
    new_obj = CreateObj()
    new_obj.new_obj(valid_create_payload)
    new_obj.check_response_is_200()
    new_obj.validate(new_obj.get_data())
    payload_data = valid_create_payload['data']
    assert new_obj.get_name() == valid_create_payload['name'], \
        f"Сервер вернул {new_obj.get_name()}"
    # assert new_obj.get_year() == payload_data['year'], f"Сервер вернул {new_obj.get_year()}"
    # assert new_obj.get_price() == payload_data['price'], f"Сервер вернул {new_obj.get_price()}"
    # assert new_obj.get_cpu_model() == payload_data['CPU model'], f"Сервер вернул {new_obj.get_cpu_model()}"
    # assert new_obj.get_hard_disk_size() == payload_data['Hard disk size'], f"Сервер вернул {new_obj.get_hard_disk_size()}"
    assert new_obj.get_payload_data() == payload_data
