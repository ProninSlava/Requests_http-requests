from pprint import pprint
import requests

def heroes_intelligence():
    list_heroes = ['Hulk', 'Captain America', 'Thanos']
    url = 'https://superheroapi.com/api/2619421814940190/search/'
    dict_heroes_intelligence = {}

    for name in list_heroes:
        url_name = url + name
        req = requests.get(url_name).json()
        for i in req['results']:
            intelligence_heroes = i['powerstats']['intelligence']
            if name not in dict_heroes_intelligence:
                dict_heroes_intelligence[name] = int(intelligence_heroes)
#____________________________________________________________________________
    stats_maxamount = 0
    stats_maxname = ''

    for maxname, maxamount in dict_heroes_intelligence.items():
        if maxamount > stats_maxamount:
            stats_maxamount = maxamount
            stats_maxname = maxname
    print()
    print(stats_maxname)
#______________________________________________________________________________


if __name__ == '__main__':
    heroes_intelligence()



