import requests
import json
from bs4 import BeautifulSoup as bs
import os

r = requests.get("https://xn--80aesfpebagmfblc0a.xn--p1ai/information/")
soup = bs(r.content, "html5lib")
data = json.loads(soup.find("cv-stats-virus")[":stats-data"])
data2 = json.loads(soup.find("cv-stats-virus")[":charts-data"])
data3 = data2[0]
sick_difference = data['sickChange']
healed_difference = data['healedChange']
died_difference = data['diedChange']
date_today = data3['date']
sick_today = data['sick']
healed_today = data['healed']
died_today = data['died']
vaccine_first_component = data['vaccineFirst']
vaccine_total = data['vaccineSecond']

output = f'⚠ Информация на *{date_today}* \n📈 Выявлено случаев: {sick_today} *({sick_difference})* \n👨‍⚕️ ' \
                f'Выздоровело: {healed_today} *({healed_difference})* \n☠ Смертей за всё время: {died_today} *({died_difference})*' \
                f'\n_Информация: стопкоронавирус.рф_'
today_output = f'⚠ Статистика за сегодняшний день *({date_today}):* \n📈 Новые случаи: ' \
                    f'*{sick_difference}* \n👨‍⚕️ Выздоровело: *{healed_difference}* \n☠ Смертей: *{died_difference}*' \
                    f'\n_Информация: стопкоронавирус.рф_'
vaccine_output = f'🦾Вакцинировано первым компонентом: *{vaccine_first_component}*\n' \
                f'💉Полная вакцинация: *{vaccine_total}*'

os.remove('vaccine.txt')
fv = open('vaccine.txt', 'w', encoding="utf-8")
fv.write(vaccine_output)
fv.close()
os.remove('stat.txt')
f = open('stat.txt', 'w', encoding="utf-8")
f.write(output)
f.close()
os.remove('today.txt')
f1 = open('today.txt', 'w', encoding="utf-8")
f1.write(today_output)
f1.close()
