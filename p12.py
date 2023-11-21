import math
def triad():
    list1=[]
    list2=[]
    count=0
    for j in range(3,17,1):
        list1.append(j)
    for j in range(3,50,1):
        list2.append(j)    
    for k in range(0,len(list1),1):    
        for i in range(0,len(list2),1):
            d=math.sqrt((list1[k]*list1[k])+(list2[i]*list2[i]))
            if(d==int(d)):
                print("Square of(",list1[k],")","+","Square of(",list2[i],") =Square(",d,")-  So(",list1[k],",",list2[i],",",d,")is a triad")
                count=count+1
                print()
    print("Total number of triads=",count)
triad()
