import datetime
import requests
import json
from bs4 import BeautifulSoup as bs
import os

a = datetime.time(8, 30)
now = datetime.datetime.now()
nowtime = now.strftime("%H:%M")
if nowtime >= str(a):
    r = requests.get("https://xn--80aesfpebagmfblc0a.xn--p1ai/information/")
    soup = bs(r.content, "html5lib")
    data = json.loads(soup.find("cv-stats-virus")[":charts-data"])
    data_today = data[0]
    data_tomorrow = data[1]
    if data_today['sick'] > data_tomorrow['sick']:
        sick_difference = data_today['sick'] - data_tomorrow['sick']
        emoji_sick = '📈'
    elif data_today['sick'] == data_tomorrow['sick']:
        sick_difference = '+0'
        emoji_sick = '❌'
    healed_difference = data_today['healed'] - data_tomorrow['healed']
    died_difference = data_today['died'] - data_tomorrow['died']
    date_today = data_today['date']
    sick_today = data_today['sick']
    healed_today = data_today['healed']
    died_today = data_today['died']
    output = f'⚠ Информация на *{date_today}* \n{emoji_sick} Болеет: {sick_today} *(+{sick_difference})* \n👨‍⚕️ ' \
                f'Выздоровело: {healed_today} *(+{healed_difference})* \n☠ Смертей: {died_today} *(+{died_difference})*' \
                f'\n_Информация: стопкоронавирус.рф_'
    today_output = f'⚠ Статистика за сегодняшний день *({date_today}):* \n{emoji_sick} Новые случаи: ' \
                    f'*{sick_difference}* \n👨‍⚕️ Выздоровело: *{healed_difference}* \n☠ Смертей: *{died_difference}*' \
                    f'\n_Информация: стопкоронавирус.рф_'

    doutput = f'<a:warninggif:902234793801027664> Информация на **{date_today}** ' \
                f'\n<a:graphgif:902281245248094248> Болеет: {sick_today} **(+{sick_difference})**\n' \
                f'<a:nursegif:902441835639746600> Выздоровело: {healed_today} **(+{healed_difference})** ' \
                f'\n<a:skullgif:902452478392537088> Смертей: {died_today} **(+{died_difference})** \n_Информация: ' \
                f'стопкоронавирус.рф_'
    dtoday_output = f'<a:warninggif:902234793801027664> Статистика за сегодняшний день **({date_today}):** ' \
                    f'\n<a:graphgif:902281245248094248> Новые случаи: **{sick_difference}** \n' \
                    f'<a:nursegif:902441835639746600> Выздоровело: **{healed_difference}** \n' \
                    f'<a:skullgif:902452478392537088> Смертей: **{died_difference}** ' \
                    f'\n_Информация: стопкоронавирус.рф_'
    os.remove('stat.txt')
    f = open('stat.txt', 'w', encoding="utf-8")
    f.write(output)
    f.close()
    os.remove('today.txt')
    f1 = open('today.txt', 'w', encoding="utf-8")
    f1.write(today_output)
    f1.close()

    fd = open('dstat.txt', 'w', encoding="utf-8")
    fd.write(doutput)
    fd.close()
    fd1 = open('dtoday.txt', 'w', encoding="utf-8")
    fd1.write(dtoday_output)
    fd1.close()
    print('PARSED NEW INFO')
else:
    f = open('stat.txt', 'r', encoding="utf-8")
    output = f.read()
    f.close()
    print('USED OLD INFO')
