#-*-coding:UTF-8 -*-
#  EX04_05.py
#
#  �ϥ� yield ���� range() 
#  

def myrange(n):
    x = 0
    while True:
        yield x
        x += 1
        if x == n:
            break 
r=myrange(10)
for i in r:
    print(i)
print(list(r))           
#print(list(myrange(10)))