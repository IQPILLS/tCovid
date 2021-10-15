import logging

from aiogram import Bot, Dispatcher, executor, types

"""
A tool for obtaining statistics on new cases of COVID-19

email: vewaa@vk.com
Source code: https://github.com/Vewaa

Released under GNU General Public License v3.0
"""

API_TOKEN = 'YOUR BOT TOKEN'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЭтот бот создан для мониторинга статистики заболеваний COVID-19. \nДанные "
                        "обновляются каждый день в 12:00 по МСК. \n*Список команд: /help*", parse_mode='Markdown')


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("\n*Доступные команды*: \n*/start* - _Информация о боте_\n*/help* - _Список команд_\n*/stat* - "
                        "_Статистика за всё время_\n/*today* - _Статистика случаев за сегодня_", parse_mode='Markdown')


@dp.message_handler(commands=['stat'])
async def stat(message: types.Message):
    f = open('stat.txt', 'r', encoding="utf-8")
    output = f.read()
    f.close()
    await message.answer(output, parse_mode='Markdown')


@dp.message_handler(commands=['today'])
async def today(message: types.Message):
    f = open('today.txt', 'r', encoding="utf-8")
    today_output = f.read()
    f.close()
    await message.answer(today_output, parse_mode='Markdown')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)