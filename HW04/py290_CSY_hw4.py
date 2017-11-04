#-*-coding:UTF-8 -*-

#zipcode字典結構
zipcode = {
"台北市":{"中正區": 100, "大同區": 103, "中山區": 104, "松山區": 105, "大安區": 106, "萬華區": 108, "信義區": 110, "士林區": 111, "北投區": 112, "內湖區": 114, "南港區": 115, "文山區": 116}, 
"基隆市":{"仁愛區": 200, "信義區": 201, "中正區": 202, "中山區": 203, "安樂區": 204, "暖暖區": 205, "七堵區": 206},
"新北市": {"萬里區": 207, "金山區": 208, "板橋區": 220, "汐止區": 221, "深坑區": 222, "石碇區": 223, "瑞芳區": 224, "平溪區": 226, "雙溪區": 227, "貢寮區": 228, "新店區": 231, "坪林區": 232, "烏來區": 233, "永和區": 234, "中和區": 235, "土城區": 236, "三峽區": 237, "樹林區": 238, "鶯歌區": 239, "三重區": 241, "新莊區": 242, "泰山區": 243, "林口區": 244, "蘆洲區": 247, "五股區": 248, "八里區": 249, "淡水區": 251, "三芝區": 252, "石門區": 253}}



#3、zip_to_area(zip)
#傳入值為郵遞區號110、201回傳區域名稱(信義區)
#ex. 呼叫 area_to_zip(106) ，回傳 "大安區"
'''
def zip_to_area(n,m):
    print(n,m,'的區域名稱:',zipcode[n][m])
i = 0
while i < 1 :      
    CityName = input('1、請輸入要找的區域名稱位於「台北市、新北市、基隆」哪一處:')
    Zipcode_city_area = input('2、請輸入要找的郵遞區號，將回傳區域名稱：')
    zip_to_area(CityName,Zipcode_city_area)
'''
'''
#print('的區域名稱:',zipcode["新北市"])
Zipcode_city_area = '207'
cityname_get = zipcode.get("新北市")
i = 0

#if cityname_get.has(Zipcode_city_area):
 #           print(cityname_get)
try:
    return cityname_get.values().index(207)

except ValueError:
    pass
'''
#mydict = {'george':16,'amber':19}
#print (mydict.keys()[mydict.values().index(16)]) # Prints george

mydict = {'george':16,'amber':19}
#print(list(zipcode.keys())[list(zipcode.values()).index(100)]) # Prints george
print (zipcode.values)
print()
print (list(zipcode.values()))