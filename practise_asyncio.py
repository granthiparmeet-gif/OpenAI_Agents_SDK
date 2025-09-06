import asyncio

async def dowork():
    await asyncio.sleep(2)
    return "work done!"

async def main():
    print("hello there")
    result = await dowork()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())