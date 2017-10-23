'''
Q1. 使⽤set型別完成下列問題: 本班期末考試
u 數學及格的有: Tom, John, Mary, Jimmy, Sunny, Amy
u 英⽂及格的有: John, Mary , Tony , Bob , Pony, Tom , Alice
u 分別印出數學及格但英⽂不及格的名單，數學不及格
但英⽂及格的名單，兩科都及格的名單
u 最後印出全班總共有幾個同學
'''
Math_pass={'Tom', 'John', 'Mary', 'Jimmy', 'Sunny', 'Amy'}
Eng_pass={'John', 'Mary' , 'Tony','Bob','Pony','Tom' ,'Alice'}
Math_pass_butEng_unpass_list=Math_pass - Eng_pass#'Jimmy', 'Sunny', 'Amy'
Math_unpass_butEng_pass_list=Eng_pass - Math_pass#'Tony', 'Bob', 'Alice', 'Pony
MathandEng_allpass_list=Math_pass & Eng_pass#John', 'Mary', 'Tom'
Allclassmate= Math_pass | Eng_pass#'Tom', 'Bob', 'Amy', 'Sunny', 'Jimmy', 'Alice', 'Tony', 'Mary', 'John', 'Pony'
print("Q1")
print("數學通過者：", Math_pass)
print("英文通過者：",Eng_pass)
print("數學及格但英⽂不及格的名單：",Math_pass_butEng_unpass_list)
print("數學不及格但英⽂及格的名單：",Math_unpass_butEng_pass_list)
print("兩科都及格的名單：",MathandEng_allpass_list)
print("全班同學共幾位：",len(Allclassmate),"位")
print("/Q1")

'''
Q2. 使⽤dict，list 型別完成下列問題:
Tom 作業成績為 80, 100, 90, 95，
John 作業成績為 100,93,75,80
請以dict 型別存放兩個同學的資料
key:名字，value:分數列表(list)
請分別算出兩位同學的平均分數並且印出
'''
d = {'Tom': [80,100,90,95],'John': [100,93,75,80]}
Tom_avg=d.get('Tom')
John_avg=d.get('John')
print("Q2")
print ("Tom平均分數:",sum(Tom_avg)/len (Tom_avg),"分")#91.25
print ("John平均分數:",sum(John_avg)/len (John_avg),"分")#87
print("/Q2")