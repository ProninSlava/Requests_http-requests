from pprint import pprint
import requests

url_id = 'https://superheroapi.com/api/2619421814940190/search/'
url_intelligence = 'https://superheroapi.com/api/2619421814940190/'
dict_heroes_intelligence = {}
class Heroes:
    def __init__(self, name_heros, intelligence_heros = 0, id_heros = ''):
        self.name = name_heros
        self.intelligence = intelligence_heros
        self.id = id_heros
        dict_heroes_intelligence[self.name] = self.id

    def print_info(self):
        print(f'Имя_героя: {self.name} \nID_героя: {self.id} \nИнтеллект_героя: {self.intelligence} \n')

    def id_heroes(self):
            url_name = url_id + self.name
            req = requests.get(url_name).json()
            for i in req['results']:
                if 'id' in i:
                    self.id = i['id']

    def intelligence_heroes(self):
            url_name = url_intelligence + str(self.id) + '/powerstats'
            req = requests.get(url_name).json()
            self.intelligence = req['intelligence']
            dict_heroes_intelligence[self.name] = int(self.intelligence)

def best_intelligence_heroes():
    stats_maxamount = 0
    stats_maxname = ''

    for maxname, maxamount in dict_heroes_intelligence.items():
        if maxamount > stats_maxamount:
            stats_maxamount = maxamount
            stats_maxname = maxname
    print()
    print(f'Герой сс самым высоким интеллектом это: {stats_maxname}!')

Heroes1 = Heroes('Thanos')
Heroes2 = Heroes('Captain America')
Heroes3 = Heroes('Hulk')

Heroes1.id_heroes()
Heroes1.intelligence_heroes()
Heroes1.print_info()

Heroes2.id_heroes()
Heroes2.intelligence_heroes()
Heroes2.print_info()

Heroes3.id_heroes()
Heroes3.intelligence_heroes()
Heroes3.print_info()

best_intelligence_heroes()
