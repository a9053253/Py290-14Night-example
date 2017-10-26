#-*-coding:UTF-8 -*-
# For迴圈n*n乘法

N_multiplied_N = int(input('for迴圈請輸入小於10的數字:'))
if N_multiplied_N <10:
    for i in range(1, N_multiplied_N + 1, +1):
    
        for j in range(1, N_multiplied_N + 1, +1):
            print(i,'*',j,'=',i*j)
#N_multiplied_N_while = int(input('暫停'))

# While迴圈n*n乘法
#-*-coding:UTF-8 -*-
N_multiplied_N = int(input('while迴圈請輸入小於10的數字:'))
if N_multiplied_N < 10:
    i=0
    while i < N_multiplied_N:
        i = i + 1
        j=0
        while j < N_multiplied_N:
            j = j + 1
        #print(i)
            print(i,'*',j,'=',i*j)
N_multiplied_N_while = int(input('STOP'))


