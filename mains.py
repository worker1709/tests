from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor

bot = Bot(token='5796930762:AAGL0zb6R9u88wz3IermC-3wRFFwmifbQxo')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Hello world!!!')
    
@dp.message_handler()
async def start(message: types.Message):
    await message.answer('Hello world!!!')


executor.start_polling(dp, skip_updates=True)
