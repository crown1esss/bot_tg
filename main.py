import datetime
import json
import math

from usd import take_usd
from weather import take_weather
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text


TOKEN = 'secret'
bot = Bot(token=TOKEN , parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)



def commands(dp):
    @dp.message_handler(commands=['start'])
    async def get_text_message(msg: types.Message):
        start_buttons = ['Расписание','Погода','usd/rub', 'help']
        keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keybord.add(*start_buttons)
        await msg.answer('Привет ! ' , reply_markup=keybord)

    @dp.message_handler(Text(equals='help'))
    async def process_help_command(msg: types.Message):
        await msg.reply('Ну ты слишком тупой , если тебе нужна помощь в таком просто боте')

    @dp.message_handler(Text(equals='Расписание'))
    async def shedule(msg: types.Message):
        const = datetime.date(2021, 9, 1)
        y = datetime.date.today()
        week = y - const
        week = str(week).split()
        week = int(week[0]) / 7
        week = math.ceil(week)
        week_day = datetime.datetime.today().isoweekday()
        if week_day == 1 :
            name = 'monday'
            if week%2 == 1 :
                with open(f'data/{name}_chet.json') as file:
                    shedule_dict = json.load(file)
                    await msg.answer(shedule_dict)
            if week % 2 == 0:
                with open(f'data/{name}_nechet.json') as file:
                    shedule_dict = json.load(file)
                    await msg.answer(shedule_dict)

        elif week_day == 2:
            name = 'tuesday'
            if week%2 == 1 :
                with open(f'data/{name}_chet.json') as file:
                    shedule_dict = json.load(file)
                    await msg.answer(shedule_dict)
            if week % 2 == 0:
                with open(f'data/{name}_nechet.json') as file:
                    shedule_dict = json.load(file)
                    await msg.answer(shedule_dict)

        elif week_day == 3:
            name = 'wednesday'
            if week%2 == 1 :
                with open(f'data/{name}_chet.json') as file:
                    shedule_dict = json.load(file)
                    await msg.answer(shedule_dict)
            if week % 2 == 0:
                with open(f'data/{name}_nechet.json') as file:
                    shedule_dict = json.load(file)
                    await msg.answer(shedule_dict)

        elif week_day == 4:
            name = 'thursday'
            if week%2 == 1 :
                with open(f'data/{name}_chet.json') as file:
                    shedule_dict = json.load(file)
                    await msg.answer(shedule_dict)
            if week % 2 == 0:
                with open(f'data/{name}_nechet.json') as file:
                    shedule_dict = json.load(file)
                    await msg.answer(shedule_dict)

        elif week_day == 5:
            name = 'friday'
            if week%2 == 1 :
                with open(f'data/{name}_chet.json') as file:
                    shedule_dict = json.load(file)
                    await msg.answer(shedule_dict)
            if week % 2 == 0:
                with open(f'data/{name}_nechet.json') as file:
                    shedule_dict = json.load(file)
                    await msg.answer(shedule_dict)
        elif week_day == 6:
            name = 'saturday'
            if week%2 == 1 :
                with open(f'data/{name}_chet.json') as file:
                    shedule_dict = json.load(file)
                    await msg.answer(shedule_dict)
            if week % 2 == 0:
                with open(f'data/{name}_nechet.json') as file:
                    shedule_dict = json.load(file)
                    await msg.answer(shedule_dict)
        elif week_day == 7:
            await msg.answer('<b>Выходной</b>')



    @dp.message_handler(Text(equals='Погода'))
    async def get_weather(msg: types.Message):
        with open('data/weather.json') as file :
            weather_dict = json.load(file)
            temperature = weather_dict['Температура :']
            feeling = weather_dict['Ощущается как :']
            condition = weather_dict['Над головой :']
            await msg.answer(f'Температура : <b>{temperature}</b>')
            await msg.answer(f'Ощущается как : <b>{feeling}</b>')
            await msg.answer(f'Над головой :  <b>{condition}</b>')
    @dp.message_handler(Text(equals='usd/rub'))
    async def get_weather(msg: types.Message):
        with open('data/usd.json') as file :
            usd_dict = json.load(file)
            usd = usd_dict[' 1 долар =  ']
            await msg.answer(f'1 доллар стоит :  <b>{usd}</b>')


def main(dp):
    take_usd()
    take_weather()
    commands(dp)
    executor.start_polling(dp)

if __name__ == '__main__':

    main(dp)




