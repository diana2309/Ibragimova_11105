#4 variant
import asyncio
import random

# lst_my_phrases = []
lst_troll_phrases = ['АХАХАХАХАЗАЗАЗАЗЗ', 'КАК ЖЕ ТЫ ГОРИШЬ', "Олололо", "Хаха, затролено", 'ЛАЛАЛАЛАЛАЛАЛЛА', 'заскамила мамонта', 'словил на ошибке', 'гг тима раков']

async def inputt():
    while True:
        n = input()
        lst_troll_phrases.append(n)
        await asyncio.sleep(random.randrange(5))

async def troll():
    while True:
        for i in lst_troll_phrases:
            print(lst_troll_phrases[random.randrange(len(lst_troll_phrases))])
            await asyncio.sleep(random.randrange(3))


async def main():
    task1 = asyncio.create_task(troll())
    task2 = asyncio.create_task(inputt())

    await task1
    await task2

asyncio.run(main())