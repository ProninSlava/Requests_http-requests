from pprint import pprint
import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = ''
headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

def upload_file(loadfile, savefile, replace=False):
    res = requests.get(f'{URL}/upload?path={savefile}&overwrite={replace}', headers=headers).json()
    pprint(res)
    with open(loadfile, 'rb') as f:
        try:
            requests.put(res['href'], files={'file':f})
        except KeyError:
            print(res)

upload_file(r'E:\Python\Упражнения\DZ8\yandex.txt', 'netology/yandex.txt')


