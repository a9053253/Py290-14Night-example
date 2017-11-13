import random
import time
import os
import shutil
'''
file = open('rand_num.txt', 'w', encoding = 'UTF-8')
for i in range(100):
    a =str(random.randint(1,1000))+'\n'
    file.write(a)
    print (a)
file.close()
'''

nums = range(1,1001,2)
for n in random.sample(num,100):
    print(n,file=open('random.txt'),'\a')
    print('ctime:',time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    os.makedir("test")
    shutil.move("random.txt",".\\test\\random.txt")
'''
u 建立一個檔案random.txt檔案內容為
u 生成 100個1~1000的奇數存入檔案
(一個數字一行，且數 字不重複)
u 使用os模組讀取此檔案
u 使用time模組將此檔案的印出建立日期、修改日期
u 建立一個名為test的目錄
u 使用shutil模組將random.txt移動至test目錄下
'''
