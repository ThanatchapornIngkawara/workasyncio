# example of an asynchronous iterator with async for loop
import asyncio
import time

# define an asynchronous iterator
class AsyncIterator():
    # constructor, define some state
    def __init__(self):
        self.counter = 0
    
    # create an instance o the iterator
    def __aiter__(self):
        return self
    
    # return the next awaitable
    async def __anext__(self):
        # check for no furture items
        if self.counter >= 10:
            raise StopAsyncIteration
        # increment the counter
        self.counter += 1
        # simulate work
        await asyncio.sleep(1)
        # return the counter value
        return self.counter
# main coroutine
async def main():
    # loop over async iterator with async for loop
    async for item in AsyncIterator():
        print(f'{time.ctime()}{item}')
# execute the asyncio program
asyncio.run(main())

# Wed Jul 19 14:55:44 20231
# Wed Jul 19 14:55:45 20232
# Wed Jul 19 14:55:46 20233
# Wed Jul 19 14:55:47 20234
# Wed Jul 19 14:55:48 20235
# Wed Jul 19 14:55:49 20236
# Wed Jul 19 14:55:50 20237
# Wed Jul 19 14:55:51 20238
# Wed Jul 19 14:55:52 20239
# Wed Jul 19 14:55:53 202310
