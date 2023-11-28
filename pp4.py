def count20(num):
    list1=[]
    file1=open("words6.txt","r")
    list1=file1.readlines()
    res=(list1[num-1])
    return res
print("This program works only upto 120")
num1=int(input("Enter a number"))
if(num1<=20):
    result=count20(num1)
    print(result)
elif(20<num1<30):
    r=num1%10
    q=num1//10
    word1=count20((q)*10)
    word2=count20(r)
    print(word1, word2, end=" ")
elif(30<=num1<110):
    r=num1%10
  
    q=num1//10
    if(r==0):
        word1=count20(20+(q-2))
        print(word1)
    else:
        word1=count20(20+(q-2))
        word2=count20(r)
        print(word1,word2, end=" ")
elif(num1>=110):
    r1=num1%100
    q=num1//100
    word1=count20(20+((q*10)-2))
    word2=count20(r1)
    print(word1,word2)

