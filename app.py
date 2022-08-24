import logging

from aiogram import Bot, Dispatcher, executor, types
from mongo import get_database

"""
A tool for obtaining statistics on new cases of COVID-19

email: iliasovanton@yandex.ru
Source code: https://github.com/Vewaa

Released under GNU General Public License v3.0
"""

token = ''

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЭтот бот создан для мониторинга статистики заболеваний COVID-19. \nДанные "
                        "обновляются каждый день не ранее 11:30 по МСК. \n*Список команд: /help*", parse_mode='Markdown')
    user_id = str(message.chat.id)
    print('Вызов команды /start', user_id)
    dbname = get_database()
    db = dbname["accounts"]
    item_details = db.find()
    for item in item_details:
        if user_id in item.values():
            break
    else:
        await bot.send_message('229629831', f"Новый пользователь: @{message.chat.username} \nАйди чата: {user_id}")
        add = {
            "telegram_id": user_id}
        db.insert_one(add)


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("*Доступные команды*: \n*/start* - _Информация о боте_\n*/help* - _Список команд_\n*/stat* - "
                        "_Статистика за всё время_\n*/today* - _Статистика случаев за сегодня_", parse_mode='Markdown')


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
    user_id = str(message.chat.id)
    print('Вызов команды /today', user_id)


@dp.message_handler(commands=['vaccine'])
async def vaccine(message: types.Message):
    import timechecker
    f = open('vaccine.txt', 'r', encoding="utf-8")
    vaccine_output = f.read()
    f.close()
    await message.answer(vaccine_output, parse_mode='Markdown')


@dp.message_handler(commands=['virus'])
async def virus(messages: types.Message):
    await bot.send_photo(chat_id=messages.chat.id, photo='https://i.imgur.com/oz7GCqF.png')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
