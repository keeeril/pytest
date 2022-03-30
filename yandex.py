import requests

with open('/Users/keeeril/Desktop/token.txt', 'rt', encoding='utf-8') as file:
    token = file.readline()

def create_folders(path: str):
    params = {'path': path}
    headers = {
            "Accept": "application/json",
            "Authorization": "OAuth " + token
    }

    url = "https://cloud-api.yandex.net/v1/disk/resources"
    r = requests.put(url=url, params=params, headers=headers)
    return r.status_code

def delete_folders(path: str):
    headers = {
            "Accept": "application/json",
            "Authorization": "OAuth " + token
    }
    params = {'path': path}

    url = "https://cloud-api.yandex.net/v1/disk/resources"
    r = requests.delete(url=url, params=params, headers=headers)
    return r.status_code

print(create_folders('testing'))
print(delete_folders('testing'))
