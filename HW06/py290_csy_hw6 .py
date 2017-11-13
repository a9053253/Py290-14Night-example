#-*-coding:UTF-8*-*-

file = open('stores_old.csv','r',encoding='big5')
file2= open('stores_new.csv','w',encoding='big5')
for line in file.readlines():
    #print(line,end='')

    line2= line.split(',')
    print(line2[0],line2[3],line2[5],line2[6])
    line3=str(line2[0]+';'+line2[3]+';'+line2[5]+';'+line2[6]+';'+'\n')
    file2.write(line3)
    #print(line2)
file.close()
file2.close()


#0sid,3name,5tel,6wifi,
#0sid,1longitude,2latitude,3name,4address,5tel,6wifi,7notes
#1,121.740089,25.132571,海景門市,200基隆市仁愛區港西街6之2號,02-2428-4223,Y,
'''
import re
a='Beautiful, is; better*than\nugly'
# 四个分隔符为：,  ;  *  \n
x= re.split(',|; |\*|\n',a)
print(x)
'''
