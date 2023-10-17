from aiogram import Dispatcher
from aiogram.dispatcher.middlewares import BaseMiddleware
from .admin_keyboards.reply_admin import middlewares_status
from data.loader import dp
from aiogram.types import Message
from aiogram.types import Message

from data.loader import dp
from .admin_keyboards.reply_admin import middlewares_status

bot_status = True


@dp.message_handler(regexp='🤖Бот')
async def collect_bot_status(message: Message):
    await message.answer('Выключить включить', reply_markup=middlewares_status())


@dp.message_handler(regexp='Включить')
async def on_bot(message: Message):
    global bot_status
    bot_status = True
    await message.answer('Бот работает')


@dp.message_handler(regexp='Отключить')
async def off_bot(message: Message):
    global bot_status
    bot_status = False
    await message.answer('Бот выключен')



class Bot_worker(BaseMiddleware):

    bot_status = True

    async def check_status(self, bot_status):
        if not bot_status:
            await bot.close_bot