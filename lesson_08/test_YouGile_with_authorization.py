import requests

import confiq


# def test_get_company_list():
#     resp = requests.post(base_url + "/auth/companies",
#                          headers={"Content-Type": "application/json"},
#                          json=body_for_get_list_company)
#     response = resp.json()
#     first_company = response["content"][0]
#     company_id = first_company.get("id")
#     assert bool(company_id)


# def get_key():
#     resp = requests.post(base_url + "/auth/companies",
#                          headers={"Content-Type": "application/json"},
#                          json=body_for_get_list_company)
#     company_id = resp.json()["content"][0]["id"]
#     body_for_get_key = {
#         "login": login,
#         "password": password,
#         "companyId": company_id
#         }
#     resp_key = requests.post(base_url + "/auth/keys", headers={"Content-Type": "application/json"},
#                              json=body_for_get_key)
#     key = resp_key.json()["key"]
#     return key


def create_project():
    body_create_project = {
         "title": "YouGile",
         "users": confiq.user_role
             }
    resp = requests.post(confiq.base_url + "/projects",
                         headers=confiq.headers_for_projects,
                         json=body_create_project)
    return resp


def get_project_by_id(project_id):
    result = requests.get(confiq.base_url + "/projects/" + str(project_id),
                          headers=confiq.headers_for_projects)
    return result


def change_project():
    project_id = create_project().json()["id"]
    result = requests.put(confiq.base_url + "/projects/" + project_id,
                          headers=confiq.headers_for_projects,
                          json=confiq.body_change_project)
    return result


def test_create_project():
    response = create_project()
    assert response.status_code == 201


def test_create_project_negative():  # тело запроса без названия проекта
    body_create_project = {
        "title": "",
        "users": confiq.user_role
        }
    resp = requests.post(confiq.base_url + "/projects", headers=confiq.headers_for_projects, json=body_create_project)
    assert resp.status_code == 400


def test_get_project_by_id():
    project_id = create_project().json()["id"]
    result = get_project_by_id(project_id)
    project_id_new = result.json()["id"]
    assert result.status_code == 200
    assert project_id == project_id_new


def test_get_project_by_id_negative():
    fake_id = "00000000-0000-0000-0000-000000000000"
    result = get_project_by_id(fake_id)

    # Ожидаем 404 Not Found или 400 Bad Request
    assert result.status_code in (404, 400)
    # Проверяем наличие сообщения об ошибке
    assert "error" in result.json()


def test_change_project():
    resp = change_project()
    project_changed_id = resp.json()["id"]
    assert resp.status_code == 200
    get_response = requests.get(confiq.base_url + "/projects/" + str(project_changed_id),
                                headers=confiq.headers_for_projects)
    assert get_response.json()["title"] == confiq.body_change_project["title"]


def test_delete_project():
    project_id = create_project().json()["id"]
    body_change_project = {
        "deleted": True
             }
    result = requests.put(confiq.base_url + "/projects/" + project_id,
                          headers=confiq.headers_for_projects, json=body_change_project)
    assert result.status_code == 200
    get_response = requests.get(confiq.base_url + "/projects/" + project_id, headers=confiq.headers_for_projects)
    assert get_response.json()["deleted"] is True


def test_change_project_negative():  # несуществующий id проекта
    unrealistic_id = "12345"
    result = requests.put(confiq.base_url + "/projects/" + unrealistic_id, headers=confiq.headers_for_projects)
    assert result.json()["message"] == "Проект не найден"
