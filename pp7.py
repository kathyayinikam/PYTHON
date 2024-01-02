import csv
list1=[]
f1=open("Holidays_2024.csv","r")
info1=csv.reader(f1)
for line in info1:
    list1.append(line)

date1=[]
day1=[]
holiday1=[]
state1=[]
len1=len(list1)

date2=[]
day2=[]
holiday2=[]
state2=[]

date3=[]
day3=[]
holiday3=[]
state3=[]
for i in range(0,len1,1):
    date1.append(list1[i][0])
    day1.append(list1[i][1])
    holiday1.append(list1[i][2])
    state1.append(list1[i][3].replace("\n","").replace("&",","))
print("All holidays")
for i in range(0,len1,1):
        if("KA" in state1[i]):
            print(date1[i],day1[i],holiday1[i],"is a holiday for Karnataka")
            date2.append(date1[i])
            day2.append(day1[i])
            holiday2.append(holiday1[i])
            state2.append(state1[i])
len2=len(date2)
print("")
print("")
print("Excluding the National except")
for i in range(0,len2,1):
    if("National except" not in state2[i] and "KA" in state2[i]):
            print(date2[i],day2[i],holiday2[i],"is a holiday for Karnataka")
            date3.append(date2[i])
            day3.append(day2[i])
            holiday3.append(holiday2[i])
len3=len(date3)


          

        
