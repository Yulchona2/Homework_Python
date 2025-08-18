base_url = "https://ru.yougile.com/api-v2"

login = "yulchona2@gmail.com"
password = "Ip1985YougileSkyPro"
company_name = "SkyPro"

body_for_get_list_company = {
        "login": login,
        "password": password,
        "name": company_name
        }
key = "bG-nN3IFcKZDqz8gi0cwQUdnn0kxplJgNSCtrkZSzNzvo6a2V9P0CevRQRABHeGc"

headers_for_projects = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + key
    }
body_change_project = {
        "title": "Changed_project"
             }
user_role = {"7c2db6d9-5078-488a-977d-bd6cf143f1fa": "admin"}
