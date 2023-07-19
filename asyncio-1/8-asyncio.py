# example of running a blocking io-bound task in asyncio
import asyncio
import time

# a blocking io-bound task
def blocking_task():
    # report a messenger
    print(f'{time.ctime()} Task starting...')
    # block for a while
    time.sleep(2)
    # report a messenger
    print(f'{time.ctime()} Task done')

# main coroutine
async def main():
    # report a messenger
    print(f'{time.ctime()} Main running the blocking task')
    # create a coroutine for the blocking task
    coro = asyncio.to_thread(blocking_task)
    # schedule the task
    task = asyncio.create_task(coro)
    # report a messenger
    print(f'{time.ctime()} Main doing other things')
    # allow the scheduled task to start
    await asyncio.sleep(0)
    # await the task
    await task

# run the asyncio program
asyncio.run(main())

# Wed Jul 19 15:00:52 2023 Main running the blocking task
# Wed Jul 19 15:00:52 2023 Main doing other things
# Wed Jul 19 15:00:52 2023 Task starting...
# Wed Jul 19 15:00:54 2023 Task done