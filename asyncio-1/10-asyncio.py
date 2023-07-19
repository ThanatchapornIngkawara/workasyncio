# example of an asynchronous context manager via async with
import asyncio
import time

import asyncio

# define an asynchronous context manager
class AsyncContextManager:
    # enter the async context manager
    async def __aenter__(self):
        # report a message
        print(f'{time.ctime} >entering the context manager')
        # block for a moment
        await asyncio.sleep(0.5)

    # exit the async context manager
    async def __aexit__(self, exc_type, exc, tb):
        # report a message
        print(f'{time.ctime} >exiting the context manager')
        # block for a moment
        await asyncio.sleep(0.5)

# define a simple coroutine
async def custome_coroutine():
    # create and use the asynchronous context manager
    async with AsyncContextManager() as manager:
        # report the result 
        print(f'{time.ctime} witin yhe manager')


# start the asyncio program
asyncio.run(custome_coroutine())

# <built-in function ctime> >entering the context manager
# <built-in function ctime> witin yhe manager
# <built-in function ctime> >exiting the context manager