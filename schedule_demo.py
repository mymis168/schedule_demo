#透過 schedule 排程 (獨立安裝　uv add schedule , pip install schedule)

import schedule
import time
from datetime import datetime

count=0

def task1(): 
    
    print(f"任務1 完成時間: {datetime.now()}")    

def task2(): 
    print(f"任務2 完成時間: {datetime.now()}")    


print("排程開始")
schedule.every(2).seconds.do(task1)
schedule.every(4).seconds.do(task2)

# !!!! 重要 
while True: 
    count+=1
    schedule.run_pending()   # 檢查是否有滿足/符合排程的任務 有-->執行
    if count >=10:
        schedule.clear()
        break
    time.sleep(1)            # 這一行在幹嘛????
print("程式結束")

