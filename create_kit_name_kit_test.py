import data
import sender_stand_request

def get_new_user_token():
    response = sender_stand_request.post_new_user()
    return response.json()["authToken"]

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

def positive_assert(kit_body):
    auth_token = get_new_user_token()

    response = sender_stand_request.post_new_client_kit(
        kit_body,
        auth_token
    )

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()

    response = sender_stand_request.post_new_client_kit(
        kit_body,
        auth_token
    )

    assert response.status_code == 400

def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("a")

    positive_assert(kit_body)

def test_create_kit_511_letters_in_name_get_success_response():
    kit_body = get_kit_body(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    )

    positive_assert(kit_body)

def test_create_kit_0_letter_in_name_get_error_response():
    kit_body = get_kit_body("")

    negative_assert_code_400(kit_body)

def test_create_kit_512_letters_in_name_get_error_response():
    kit_body = get_kit_body(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    )

    negative_assert_code_400(kit_body)

def test_create_kit_special_symbols_in_name_get_success_response():
    kit_body = get_kit_body("\"№%@\",")

    positive_assert(kit_body)

def test_create_kit_has_space_in_name_get_success_response():
    kit_body = get_kit_body(" A Aaa ")

    positive_assert(kit_body)

def test_create_kit_numbers_in_name_get_success_response():
    kit_body = get_kit_body("123")

    positive_assert(kit_body)

def test_create_kit_no_name_get_error_response():
    kit_body = {}

    negative_assert_code_400(kit_body)

def test_create_kit_number_type_name_get_error_response():
    kit_body = {
        "name": 123
    }

    negative_assert_code_400(kit_body)
