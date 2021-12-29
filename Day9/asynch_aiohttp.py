import asyncio

async def name():
    print("Himanshu")
    await asyncio.sleep(1)
    print("Jadon")

async def main():
    await asyncio.gather(name(), name(), name())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")