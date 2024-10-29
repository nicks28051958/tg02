import aiohttp
import asyncio

async def test_simple_weather_request():
    url = f"http://api.openweathermap.org/data/2.5/weather?lat=53.3895&lon=58.971264&units=metric&appid={WEATHER_API_KEY}&lang=ru"
    timeout = aiohttp.ClientTimeout(total=60)  # 60 секунд таймаут
    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as response:
                data = await response.json()
                print(data)
    except Exception as e:
        print(f"Ошибка при запросе данных: {e}")

if __name__ == "__main_1__":
    asyncio.run(test_simple_weather_request())
