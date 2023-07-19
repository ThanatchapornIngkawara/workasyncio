# example of waitting for all tasks to complete
import random
import asyncio
import time

# coroutine to execute in a new task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random.random()
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    print(f'{time.ctime()} >task {arg} done with {value}')

# main coroutine
async def main():
    # create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for all tasks to complete # ALL_COMPLETED, FIRST_EXCEPTION
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    #report result
    print(f'{time.ctime()} All done')

# start the asyncio program
asyncio.run(main())


# Wed Jul 12 15:07:18 2023 >task 1 done with 0.0047506908603485165
# Wed Jul 12 15:07:18 2023 >task 8 done with 0.08223354831389662
# Wed Jul 12 15:07:18 2023 >task 9 done with 0.08926423746033207
# Wed Jul 12 15:07:18 2023 >task 5 done with 0.10511413242905931
# Wed Jul 12 15:07:18 2023 >task 4 done with 0.15692797994987984
# Wed Jul 12 15:07:18 2023 >task 6 done with 0.19966212147617712
# Wed Jul 12 15:07:19 2023 >task 0 done with 0.45007825989416006
# Wed Jul 12 15:07:19 2023 >task 3 done with 0.6245446650412213
# Wed Jul 12 15:07:19 2023 >task 7 done with 0.7777792126439266
# Wed Jul 12 15:07:19 2023 >task 2 done with 0.809379193564795
# Wed Jul 12 15:07:19 2023 All done