def tables(start,stop):
    for j in range(start,stop+1,1):
        for i in range(1,11,1):
            print(j,"x",i,"=",j*i);
        print();
start=int(input("enter a number"))
stop=int(input("enter stop number"))
tables(start,stop)
