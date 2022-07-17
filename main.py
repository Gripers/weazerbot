from aiogram import Bot, Dispatcher, executor, types
import python_weather

bot = Bot(token="5481950853:AAH2pB0b8FCqPRzui2NIu9GD4vJmCa3HpK4")
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL, locale="ru-RU")

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Хэйоу, введи город чтобы узнать погоду в нем")

@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.find(message.text)
    celcius = round((weather.current.temperature -32) / 1.8)

    res_msg = weather.location_name + "\n"
    res_msg += f"Текущая температура: {celcius}°\n"
    res_msg += f"Состояние погоды: {weather.current.sky_text}"

    await message.answer(res_msg)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
