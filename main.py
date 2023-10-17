from utils.notify_admin import on_startup_notify
from utils.set_bot_commands import set_default_commands
import middlewares
from handlers.admin.activate_middlewares import check_status


async def on_startup(dp):
    middlewares.setup(dp)
    await check_status(dp)
    await on_startup_notify(dp)
    await set_default_commands(dp)
    print('Бот запущен')


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)