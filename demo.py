from schedule import every,repeat,run_pending,get_jobs,clear
import time
from datetime import datetime
looping = True

#@repeat(every(5).seconds)
def task1():
    print('test')

@repeat(every(3).seconds.until("13:34"))
def task2():
    print("until 13:31")

@repeat(every(5).seconds)
def task3():
    jobs = get_jobs()
    print(f'len: {len(jobs)}')
    if len(jobs)==1:
        looping = False



while looping:
    run_pending()
    time.sleep(1)

    