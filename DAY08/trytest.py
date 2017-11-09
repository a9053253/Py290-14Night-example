#-*-coding:UTF-8 -*-
while true :
        def num_division(n,m):
                try:
                    a= n/m
                    print ("normal",a)         	
                except Exception as err:
                    print("OS error: {0}".format(err))
                else:
                        break

'''
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
else:
        i = i + 10
      print("Open file successs.")
'''
 
            
