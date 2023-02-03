import requests
from pytest_voluptuous import S
from requests import Response

import schemas.schemas


def test_create_user():
    create_user: Response = requests.post(
        url="https://reqres.in/api/users",
        json=
        {
            "name": "Irina",
            "job": "QA"
        }
    )

    assert create_user.status_code == 201
    assert create_user.json()["name"] == "Irina"
    assert create_user.json()["job"] == "QA"
    assert S(schemas.schemas.create_single_user) == create_user.json()


def test_update_user():
    update_user: Response = requests.put(
        url="https://reqres.in/api/users/2",
        json=
        {
            "name": "Irina Rogova",
            "job": "tester"
        }
    )

    assert update_user.status_code == 200
    assert update_user.json()["name"] == "Irina Rogova"
    assert update_user.json()["job"] == "tester"
    assert update_user.json()["updatedAt"] is not None
    assert S(schemas.schemas.update_single_user) == update_user.json()


def test_delete_user():
    delete_user: Response = requests.delete(url=" https://reqres.in/api/users/2")

    assert delete_user.status_code == 204


def test_login_successful():
    login_successfully: Response = requests.post(
        url="https://reqres.in/api/login",
        json=
        {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
    )

    assert login_successfully.status_code == 200
    assert login_successfully.json()["token"] is not None
    assert S(schemas.schemas.login_successfully) == login_successfully.json()


def test_login_unsuccessful():
    login_unsuccessful: Response = requests.post(
        url="https://reqres.in/api/login",
        json=
        {
            "email": "neit.@f",
        }
    )

    assert login_unsuccessful.status_code == 400
    assert len(login_unsuccessful.content) != 0




