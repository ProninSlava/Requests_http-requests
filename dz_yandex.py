from pprint import pprint
import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

# _____________________________________________________________________________
    def get_url_upload(self, disk_file_path: str):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        h = self.get_headers()
        p = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=h, params=p)
        # pprint(response.json())
        return response.json()

#_____________________________________________________________________________
    #Загружаем файл на яндекс диск
    def upload_file_disk(self, disk_file_path: str, filename: str):
        href_json = self.get_url_upload(disk_file_path=disk_file_path)
        href = href_json['href']
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.raise_for_status() == 201:
            print('Success')

if __name__ == '__main__':

    token = 'AQAAAABe-PqUAADLWzMn3xXq0kNEoJoNHAbCHgY'
    uploader = YaUploader(token)
    result = uploader.upload_file_disk('/netology/yandex.txt', 'yandex.txt')


