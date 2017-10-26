#-*-coding:UTF-8 -*-
#For
N_multiplied_N = int(input('Please input num:'))
if N_multiplied_N <10:
    for i in range(1, N_multiplied_N, +1):
    
        for j in range(1, N_multiplied_N, +1):
            print(i,'*',j,'=',i*j)

#While