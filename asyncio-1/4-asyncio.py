# example of gather for many coroutines in a list
import asyncio
import time

# coroutine use for a tak
async def task_coro(value):
    # report a message
    print(f'{time.ctime()} task {value} executing')
    # sleep for a moment
    await asyncio.sleep(1)

# coroutine used for the entry point
async def main():
    # report a message
    print(f'{time.ctime()} main starting')
    # create many coroutines
    coros = [task_coro(i) for i in range(100)]
    # run the tasks
    await asyncio.gather(*coros)
    # report its details
    print(f'{time.ctime()} main done')


# start the asyncio program
asyncio.run(main())

# Wed Jul 12 14:50:53 2023 main starting
# Wed Jul 12 14:50:53 2023 task 0 executing
# Wed Jul 12 14:50:53 2023 task 1 executing
# Wed Jul 12 14:50:53 2023 task 2 executing
# Wed Jul 12 14:50:53 2023 task 3 executing
# Wed Jul 12 14:50:53 2023 task 4 executing
# Wed Jul 12 14:50:53 2023 task 5 executing
# Wed Jul 12 14:50:53 2023 task 6 executing
# Wed Jul 12 14:50:53 2023 task 7 executing
# Wed Jul 12 14:50:53 2023 task 8 executing
# Wed Jul 12 14:50:53 2023 task 9 executing
# Wed Jul 12 14:50:53 2023 task 10 executing
# Wed Jul 12 14:50:53 2023 task 11 executing
# Wed Jul 12 14:50:53 2023 task 12 executing
# Wed Jul 12 14:50:53 2023 task 13 executing
# Wed Jul 12 14:50:53 2023 task 14 executing
# Wed Jul 12 14:50:53 2023 task 15 executing
# Wed Jul 12 14:50:53 2023 task 16 executing
# Wed Jul 12 14:50:53 2023 task 17 executing
# Wed Jul 12 14:50:53 2023 task 18 executing
# Wed Jul 12 14:50:53 2023 task 19 executing
# Wed Jul 12 14:50:53 2023 task 20 executing
# Wed Jul 12 14:50:53 2023 task 21 executing
# Wed Jul 12 14:50:53 2023 task 22 executing
# Wed Jul 12 14:50:53 2023 task 23 executing
# Wed Jul 12 14:50:53 2023 task 24 executing
# Wed Jul 12 14:50:53 2023 task 25 executing
# Wed Jul 12 14:50:53 2023 task 26 executing
# Wed Jul 12 14:50:53 2023 task 27 executing
# Wed Jul 12 14:50:53 2023 task 28 executing
# Wed Jul 12 14:50:53 2023 task 29 executing
# Wed Jul 12 14:50:53 2023 task 30 executing
# Wed Jul 12 14:50:53 2023 task 31 executing
# Wed Jul 12 14:50:53 2023 task 32 executing
# Wed Jul 12 14:50:53 2023 task 33 executing
# Wed Jul 12 14:50:53 2023 task 34 executing
# Wed Jul 12 14:50:53 2023 task 35 executing
# Wed Jul 12 14:50:53 2023 task 36 executing
# Wed Jul 12 14:50:53 2023 task 37 executing
# Wed Jul 12 14:50:53 2023 task 38 executing
# Wed Jul 12 14:50:53 2023 task 39 executing
# Wed Jul 12 14:50:53 2023 task 40 executing
# Wed Jul 12 14:50:53 2023 task 41 executing
# Wed Jul 12 14:50:53 2023 task 42 executing
# Wed Jul 12 14:50:53 2023 task 43 executing
# Wed Jul 12 14:50:53 2023 task 44 executing
# Wed Jul 12 14:50:53 2023 task 45 executing
# Wed Jul 12 14:50:53 2023 task 46 executing
# Wed Jul 12 14:50:53 2023 task 47 executing
# Wed Jul 12 14:50:53 2023 task 48 executing
# Wed Jul 12 14:50:53 2023 task 49 executing
# Wed Jul 12 14:50:53 2023 task 50 executing
# Wed Jul 12 14:50:53 2023 task 51 executing
# Wed Jul 12 14:50:53 2023 task 52 executing
# Wed Jul 12 14:50:53 2023 task 53 executing
# Wed Jul 12 14:50:53 2023 task 54 executing
# Wed Jul 12 14:50:53 2023 task 55 executing
# Wed Jul 12 14:50:53 2023 task 56 executing
# Wed Jul 12 14:50:53 2023 task 57 executing
# Wed Jul 12 14:50:53 2023 task 58 executing
# Wed Jul 12 14:50:53 2023 task 59 executing
# Wed Jul 12 14:50:53 2023 task 60 executing
# Wed Jul 12 14:50:53 2023 task 61 executing
# Wed Jul 12 14:50:53 2023 task 62 executing
# Wed Jul 12 14:50:53 2023 task 63 executing
# Wed Jul 12 14:50:53 2023 task 64 executing
# Wed Jul 12 14:50:53 2023 task 65 executing
# Wed Jul 12 14:50:53 2023 task 66 executing
# Wed Jul 12 14:50:53 2023 task 67 executing
# Wed Jul 12 14:50:53 2023 task 68 executing
# Wed Jul 12 14:50:53 2023 task 69 executing
# Wed Jul 12 14:50:53 2023 task 70 executing
# Wed Jul 12 14:50:53 2023 task 71 executing
# Wed Jul 12 14:50:53 2023 task 72 executing
# Wed Jul 12 14:50:53 2023 task 73 executing
# Wed Jul 12 14:50:53 2023 task 74 executing
# Wed Jul 12 14:50:53 2023 task 75 executing
# Wed Jul 12 14:50:53 2023 task 76 executing
# Wed Jul 12 14:50:53 2023 task 77 executing
# Wed Jul 12 14:50:53 2023 task 78 executing
# Wed Jul 12 14:50:53 2023 task 79 executing
# Wed Jul 12 14:50:53 2023 task 80 executing
# Wed Jul 12 14:50:53 2023 task 81 executing
# Wed Jul 12 14:50:53 2023 task 82 executing
# Wed Jul 12 14:50:53 2023 task 83 executing
# Wed Jul 12 14:50:53 2023 task 84 executing
# Wed Jul 12 14:50:53 2023 task 85 executing
# Wed Jul 12 14:50:53 2023 task 86 executing
# Wed Jul 12 14:50:53 2023 task 87 executing
# Wed Jul 12 14:50:53 2023 task 88 executing
# Wed Jul 12 14:50:53 2023 task 89 executing
# Wed Jul 12 14:50:53 2023 task 90 executing
# Wed Jul 12 14:50:53 2023 task 91 executing
# Wed Jul 12 14:50:53 2023 task 92 executing
# Wed Jul 12 14:50:53 2023 task 93 executing
# Wed Jul 12 14:50:53 2023 task 94 executing
# Wed Jul 12 14:50:53 2023 task 95 executing
# Wed Jul 12 14:50:53 2023 task 96 executing
# Wed Jul 12 14:50:53 2023 task 97 executing
# Wed Jul 12 14:50:53 2023 task 98 executing
# Wed Jul 12 14:50:53 2023 task 99 executing
# Wed Jul 12 14:50:54 2023 main done