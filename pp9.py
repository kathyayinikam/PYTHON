with open("adapt.txt",encoding="UTF-8") as f1:
    list1=[]
    list1=f1.read()
    list1=list1.split(" ")
    list4=[element.lower().replace("\n","") for element in list1]
    list2=set(list4)
    list3=sorted(list2)
with open("sorted_a.txt","w",encoding="UTF-8") as f2:
    f2.write(" ".join(list3))
    print(list3)
