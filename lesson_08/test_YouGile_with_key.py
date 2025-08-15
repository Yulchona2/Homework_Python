import requests

base_url = "https://ru.yougile.com/api-v2"
key = ""  # вставить ключ
user_role = {"d0ddf6a5-4de0-48c7-b9c0-7770d4a4db60": "admin"}
headers_for_projects = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + key
    }


def create_project():
    body_create_project = {
        "title": "YouGile",
        "users": user_role
        }
    resp = requests.post(base_url + "/projects", headers=headers_for_projects, json=body_create_project)
    return resp


def get_company_by_id(project_id=None):
    if project_id is None:  # Если ID не передан, создаем новый проект
        project_id = create_project().json()["id"]
    result = requests.get(base_url + "/projects/" + project_id, headers=headers_for_projects)
    return result


def test_create_project():
    response = create_project()
    assert response.status_code == 201


def test_create_project_negative():  # тело запроса без названия проекта
    body_create_project = {
        "title": "",
        "users": user_role
        }
    resp = requests.post(base_url + "/projects", headers=headers_for_projects, json=body_create_project)
    assert resp.status_code == 400


def test_get_company_by_id():
    result = get_company_by_id()
    assert result.status_code == 200


def test_get_company_by_id_negative():  # несуществующий id проекта
    result = get_company_by_id(project_id="12345")
    assert result.status_code == 404
    assert result.json()["message"] == "Проект не найден"


def test_change_project():
    project_id = create_project().json()["id"]
    body_change_project = {
        "title": "Changed_project"
             }
    result = requests.put(base_url + "/projects/" + project_id,
                          headers=headers_for_projects, json=body_change_project)
    assert result.status_code == 200
    get_response = requests.get(base_url + "/projects/" + project_id, headers=headers_for_projects)
    assert get_response.json()["title"] == body_change_project["title"]


def test_delete_project():
    project_id = create_project().json()["id"]
    body_change_project = {
        "deleted": True
             }
    result = requests.put(base_url + "/projects/" + project_id,
                          headers=headers_for_projects, json=body_change_project)
    assert result.status_code == 200
    get_response = requests.get(base_url + "/projects/" + project_id, headers=headers_for_projects)
    assert get_response.json()["deleted"] is True


def test_change_project_negative():  # несуществующий id проекта
    unrealistic_id = "12345"
    result = requests.put(base_url + "/projects/" + unrealistic_id, headers=headers_for_projects)
    assert result.json()["message"] == "Проект не найден"
