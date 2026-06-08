#Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой
# Пример положительных тестов:
# Код ответа соответствует 200.
# Результат создания папки - папка появилась в списке файлов.
import requests
token = ''

def folder_creation(name):
    headers = {
        "Authorization": token
    }
    folder_url = f'https://cloud-api.yandex.net/v1/disk/resources?path={name}'
    folder_response = requests.put(folder_url, headers=headers)
    is_folder_really_created_response = requests.get(folder_url, headers=headers)
    return folder_response.status_code, is_folder_really_created_response.status_code

# print(folder_creation(''))