import time
import datetime
import requests


class StackOverFlow:
    def __init__(self, year, month, day):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        self.url = 'https://api.stackexchange.com/'

    def unix_time(self):
        start_date = datetime.date(self.year, self.month, self.day)
        start_date_unixtime = int(time.mktime(start_date.timetuple()))
        before_start_day = start_date - datetime.timedelta(days=1)
        before_start_day_unixtime = int(time.mktime(before_start_day.timetuple()))

        return start_date_unixtime, before_start_day_unixtime

    def get_json(self):
        """ Получение json файла """
        todate, fromdate = self.unix_time()
        files_url = f'{self.url}2.3/questions?fromdate={fromdate}&todate={todate}&order=desc&sort=activity&tagged=python&site=stackoverflow'
        response = requests.get(files_url)

        return response.json()

    def get_questions(self):
        """ Функция для получения списка вопросов"""
        dict_que = self.get_json()
        list_title = []
        for que in dict_que['items']:
            list_title.append(que['title'])

        return '\n'.join(list_title)


if __name__ == '__main__':
    a = StackOverFlow(2023, 3, 18)  # выборка даты
    print(a.get_questions())
