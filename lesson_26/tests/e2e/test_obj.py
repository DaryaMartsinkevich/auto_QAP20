from lesson_26.endpoints.create_obj import CreateObj
from lesson_26.endpoints.delete_obj import DeleteObj
from lesson_26.endpoints.get_obj import GetObj
from lesson_26.endpoints.put_obj import PutObj
from lesson_26.payload.payload import valid_create_payload, update_create_payload


def test_obj():
    create_obj = CreateObj()
    create_obj.new_obj(valid_create_payload)
    create_obj.check_response_is_200()
    create_obj.validate(create_obj.get_data())
    assert create_obj.get_data()['data'] == valid_create_payload['data'], (
        f"Ответ API {create_obj.get_data()['data']}"
        f"не совпадает с ожидаемыми данными {valid_create_payload['data']}"
    )
    assert create_obj.get_name() == valid_create_payload['name'], (
        f"Имя {create_obj.get_name()} != переданному имени"
        f"{valid_create_payload['name']}"
    )

    obj_id = create_obj.get_id()
    get_obj = GetObj()
    get_obj.get_obj(obj_id)
    get_obj.check_response_is_200()
    get_obj.validate(get_obj.get_data())
    assert get_obj.get_obj_id() == obj_id, (
        f"Полученный ID {get_obj.get_obj_id()}",
        f"не соответствует {obj_id}"
    )
    assert get_obj.get_obj_name() == valid_create_payload['name'], (
        f"Полученное имя {get_obj.get_obj_name()}",
        f"не соответствует {valid_create_payload['name']}"
    )
    assert get_obj.get_obj_data() == valid_create_payload['data'], (
        f"Полученные данные {get_obj.get_obj_data()}",
        f"не соответствуют {valid_create_payload['data']}"
    )

    update_obj = PutObj()
    update_obj.put_obj(update_create_payload, obj_id)
    update_obj.check_response_is_200()
    update_obj.validate(update_obj.get_data())
    assert update_obj.get_put_obj_id() == obj_id, (
        f"Полученный ID {update_obj.get_put_obj_id()}",
        f"не соответствует {obj_id}"
    )
    assert update_obj.get_put_obj_name() == update_create_payload['name'], (
        f"Полученное имя {update_obj.get_put_obj_name()}",
        f"не соответствует {update_create_payload['name']}"
    )
    assert update_obj.get_put_obj_data() == update_create_payload['data'], (
        f"Полученные данные {update_obj.get_put_obj_data()}",
        f"не соответствует {update_create_payload['data']}"
    )

    delete_obj = DeleteObj()
    delete_obj.delete_obj(obj_id)
    delete_obj.check_response_is_200()
    delete_obj.validate(delete_obj.get_data())
    assert delete_obj.get_delete_message() == f"Объект с ID = {obj_id} удален.", (
        f"Полученное сообщение об удалении {delete_obj.get_delete_message()}",
        f"не соответствует"
    )