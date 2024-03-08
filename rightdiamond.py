
def right(string):
    s1=string
    len1=len(s1)
    for i in range (1,len1,1):
         print(s1[0:i])
    for i in range (len1,0,-1):
         print(s1[0:i])
        

def left(string):
    s1=string
    len1=len(s1)
    k=0
    for i in range (len1+1,0,-1):
        for j in range(i):
            
            print(" ",end='')
        print(s1[0:k])
        k=k+1
    for i in range (1,len1,1):
        for j in range(i+1):
            
            print(" ",end='')
        
        print(s1[0:len1-1])
        len1=len1-1

def full(string):
    
    s1=string
    len1=len(s1)
    len2=len1-1
    k=1
    for i in range ((len1+2)//2,0,-1):
        for j in range(i-1):
            
            print(" ",end='')
        print(s1[0:k])
        k=k+2
    for i in range (1,(len1+2)//2,1):
        for j in range(0,i):
            
            print(" ",end='')
        
        print(s1[0:len2-1])
        len2=len2-2

s2=input("Enter a string")
print("Left diamond")
left(s2)
print("")
print("right diamond")
right(s2)
print("")
print("Full diamond")
full(s2)
