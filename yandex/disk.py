# 9.«Работа с библиотекой requests, http-запросы»
                        # Задача №2
# У Яндекс.Диска есть очень удобное и простое API. Для описания всех его методов существует Полигон.
# Нужно написать программу, которая принимает на вход путь до файла на компьютере и сохраняет на Яндекс.
# Диск с таким же именем.
# Все ответы приходят в формате json;
# Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
# Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен".
# HOST: https://cloud-api.yandex.net:443
# Важно: Токен публиковать в github не нужно, переменную для токена нужно оставить пустой!
import requests

class YaUploader:

    def __init__(self, token):
        self.token = token
    # Функция получения заголовков
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
    # Функция для получения ссылки на место размещения нового файла на Яндекс-диске :
    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": True }
        response = requests.get(upload_url, headers=headers, params=params)
        #pprint(response.json())
        return response.json()
    # Функция , загружающая файл на Яндекс-диск :
    def upload(self, file_path: str):
        data_link = self._get_upload_link(disk_file_path=file_path)
        #pprint(data_link)
        url = data_link.get("href")
        #print(url)
        response = requests.put(url, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("успешно")

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'HM_file_requests.txt'
    token = "..."
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)