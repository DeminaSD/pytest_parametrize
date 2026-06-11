#Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой
# Пример положительных тестов:
# Код ответа соответствует 200.
# Результат создания папки - папка появилась в списке файлов.
import requests
from pprint import pprint
import json

token = ''

def folder_creation(name):
    headers = {
        "Authorization": token
    }
    folder_url = f'https://cloud-api.yandex.net/v1/disk/resources?path={name}'
    folder_response = requests.put(folder_url, headers=headers)
    root = f'https://cloud-api.yandex.net/v1/disk/resources?path=/&limit=100'
    items_list = requests.get(root, headers=headers).json()['_embedded']['items']
    names_list = [item['name'] for item in items_list]

    return folder_response.status_code, name in names_list

print(folder_creation(''))

