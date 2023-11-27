import datetime 
from datetime import timedelta
def odd_even(card):
    cc_odd=""
    cc_even=""
    len1=len(card)

    for i in range(0,len1,1):
        if i%2==0:
            cc_odd+=card[i]
        else:
            cc_even+=card[i]
   
    return(cc_odd,cc_even)

f1=open("info.txt",'r')
f2=open("city1.txt",'w')
f3=open("city2.txt",'w')
current_date = datetime.datetime.now()
current_time = datetime.datetime.now().time()
time=str(current_time).replace(":","").replace(".","")
h = current_date.hour
m = current_date.minute
s = current_date.second
d1=current_date.day
m1=current_date.month
y1=current_date.year
time=str(h)+str(m)+str(s)
date1=str(d1)+str(m1)+str(y1)
date=(time+str(d1)+str(m1)+str(y1))
while True:
    
    info1=f1.readline()
    if not info1:
            break
    result=odd_even(info1)
    if(int(date1)%2==0):
        r1=date+result[0]
        r2=date+result[1]
    else:
        r1=date+result[0]
        r2=date+result[1]
        
    r1=date+result[0]
    r2=date+result[1]
    f2.write(r1)
    f3.write(r2)
    f3.write("\n")
    

f3.close()
f2.close()

       


