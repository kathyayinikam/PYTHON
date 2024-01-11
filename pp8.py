import os

list1=[]
for i1,i2,i3 in os.walk(os.getcwd()):#current working directory
    for i in i3:
        if(os.path.isfile(i)):
            if(i.endswith(".txt")):
                list1.append(i)
                
print(list1)
words=[]
start_a=[]
start_b=[]
start_c=[]

with open(list1[0],"r") as f1:
   print("The file selected is",list1[5]);
   for row in f1.readlines():
       words.append(row.strip())
if len(words)==0:
    print("Content not present")
else:
    words.sort()
    print(words)
    leng=len(words)
    for i in range(3,leng):
        if words[i]=='':
            print("none")
        f=words[i][0]
        if(f=="a"):
            start_a.append(words[i])
        elif(f=="b"):
            start_b.append(words[i])
        elif(f=="c"):
            start_c.append(words[i])
print(start_a)
print(start_b)
print(start_c)

        
        
    

        
    

    
            
             
 
    
    
