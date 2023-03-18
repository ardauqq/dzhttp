import requests

from pprint import pprint


class SuperHeroes:

    def __init__(self, *args):
        self.heroes = []
        for _ in args:
            self.heroes.append(_)

    def get_files_list(self):
        """ Получить json файл """
        files_url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
        self.response = requests.get(files_url)

        return self.response.json()

    def top_intelligence_heroes(self):
        """ Функция для получения топ героя по интеллекту"""

        self.get_files_list()
        top_dict = {}
        for hero in self.response.json():
            if hero['name'] in self.heroes:
                top_dict[hero['name']] = int(hero['powerstats']['intelligence'])
        print(top_dict)

        # return sorted(top_dict, key=lambda el: top_dict[el], reverse=True) выведет весь топ героев
        return sorted(top_dict, key=lambda el: top_dict[el], reverse=True)[0]


if __name__ == '__main__':
    a = SuperHeroes('Hulk', 'Thanos', 'Captain America')
    pprint(a.top_intelligence_heroes())