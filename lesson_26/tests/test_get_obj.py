from lesson_26.endpoints.get_obj import GetObj
from lesson_26.payload.payload import valid_create_payload


def test_get_obj(new_object):
    obj_id = new_object
    get_obj = GetObj()
    get_obj.get_obj(obj_id)
    get_obj.check_response_is_200()
    get_obj.validate(get_obj.get_data())

    assert get_obj.get_obj_id() == obj_id, (
        f"Полученный ID {get_obj.get_obj_id()},"
        f"не соответствует {obj_id}"
    )
