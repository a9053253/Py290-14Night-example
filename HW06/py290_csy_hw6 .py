#-*-coding:UTF-8*-*-
file = open('stores_old.csv','r',encoding='big5')
for line in file.readline():
    print(line,end=' ')
file.close()
