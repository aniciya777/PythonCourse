import asyncio
import os
import sys
from time import time

import aiofiles
import aiohttp

hashes = set()


async def get_file(number: int, url: str, session: aiohttp.ClientSession) -> None:
    """
    Функция по асинхронному получению изображения с сервера и записи его на диск.

    :param number: Номер изображения
    :param url: Ссылка на изображение
    :param session: Сессия для подключения
    """
    while True:
        print(f"Получение изображения номер {number}")
        async with session.get(url, allow_redirects=True, ssl=False) as response:
            if response.status != 200 or not response.headers.get('Content-Type', '').startswith('image/'):
                print(f"[{number}] Ошибка {response.status}, пытаемся снова", file=sys.stderr)
                continue
            data = await response.read()
            image_hash = hash(data)
            if image_hash not in hashes:
                hashes.add(image_hash)
                await write_file(number, data)
                break
            print(f"Такое изображение номер {number} уже есть, попробуем ещё раз", file=sys.stderr)


async def write_file(number: int, data: bytes) -> None:
    """
    Функция по записи изображения на диск.

    :param number: Номер изображения
    :param data: Байтовое представление изображения
    """
    print(f"Запись изображения номер {number}")
    filename = os.path.join('images', f"image_{number:03d}.jpg")
    async with aiofiles.open(filename, 'wb') as f:
        await f.write(data)


async def main(count_images: int = 30) -> None:
    """
    Функция по асинхронному получению изображений с сервера и записи их на диск.

    :param count_images: Количество изображений. По умолчанию 30
    """
    url = 'https://thispersondoesnotexist.com'
    tasks = []
    timeout = aiohttp.ClientTimeout(total=30)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        for i in range(count_images):
            task = asyncio.create_task(get_file(i + 1, url, session))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time()
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main(30))
    print(f'\nИтого: {time() - t0} секунд')
