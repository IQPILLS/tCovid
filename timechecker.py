import datetime
import time
import requests
import json
from bs4 import BeautifulSoup as bs
import os

a = datetime.time(11, 40)
while True:
    now = datetime.datetime.now()
    nowtime = now.strftime("%H:%M")
    if nowtime >= str(a):
        r = requests.get("https://xn--80aesfpebagmfblc0a.xn--p1ai/information/")
        soup = bs(r.content, "html5lib")
        data = json.loads(soup.find("cv-stats-virus")[":charts-data"])
        data_today = data[0]
        data_yesterday = data[1]
        if data_today['sick'] > data_yesterday['sick']:
            sick_difference = data_today['sick'] - data_yesterday['sick']
            emoji_sick = '📈'
        elif data_today['sick'] == data_yesterday['sick']:
            sick_difference = '+0'
            emoji_sick = '❌'
        healed_difference = data_today['healed'] - data_yesterday['healed']
        died_difference = data_today['died'] - data_yesterday['died']
        date_today = data_today['date']
        sick_today = data_today['sick']
        healed_today = data_today['healed']
        died_today = data_today['died']
        output = f'⚠ Информация на *{date_today}* \n{emoji_sick} Болеет: {sick_today} *(+{sick_difference})* \n👨‍⚕️ ' \
                 f'Выздоровело: {healed_today} *(+{healed_difference})* \n☠ Смертей: {died_today} *(+{died_difference})*'
        today_output = f'⚠ Статистика за сегодняшний день *({date_today}):* \n{emoji_sick} Новые случаи: ' \
                       f'*{sick_difference}* \n👨‍⚕️ Выздоровело: *{healed_difference}* \n☠ Смертей: *{died_difference}*'
        os.remove('stat.txt')
        f = open('stat.txt', 'w', encoding="utf-8")
        f.write(output)
        f.close()
        os.remove('today.txt')
        f1 = open('today.txt', 'w', encoding="utf-8")
        f1.write(today_output)
        f1.close()
        print('PARSED NEW INFO')
        time.sleep(14400)
    else:
        f = open('stat.txt', 'r', encoding="utf-8")
        output = f.read()
        f.close()
        print('USED OLD INFO')
        time.sleep(600)
