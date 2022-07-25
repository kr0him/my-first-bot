import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as ab
import random
from random import randint
from datetime import datetime
#токен
API_TOKEN = 'TOKEN'

#управление скриптом
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
#обработчик команд
datetime_object = datetime.now()


@dp.message_handler(commands='start')
async def start(m: types.Message):
    await m.answer(f"Привет, {m.from_user.full_name}", reply_markup = ab.mainMenu1)
@dp.callback_query_handler(text="button1")
async def button1(c: types.CallbackQuery):
    await c.message.edit_text(f"Ваш ID: {c.from_user.id} \nВаше имя: {c.from_user.full_name}", reply_markup = ab.backinline)
@dp.callback_query_handler(text="time1")
async def time1(c: types.CallbackQuery):
    await c.message.edit_text(f"Дата и время: {datetime_object}", reply_markup = ab.backinline)
@dp.callback_query_handler(text="bntRandom1")
async def bntRandom(c: types.CallbackQuery):
    await c.message.edit_text(f"Ваше число: " + str(random.randint(1, 99999)), reply_markup = ab.backinline)
@dp.callback_query_handler(text="back1")
async def back_send(c: types.CallbackQuery):
    await c.message.edit_text("Вы вернулись в главное меню", reply_markup = ab.mainMenu1)
    

        
        
        
        

#конец
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)