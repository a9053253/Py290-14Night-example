import random


import random
file = open('rand_num.txt', 'w', encoding = 'UTF-8')
for i in range(100):
    file.write( str(random.randint(1,1000))+'\n' )
file.close()