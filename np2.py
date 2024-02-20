import numpy as np  #importing numpy
file= open("in1.txt","r")#opening the text file in read mode
list1= f1.readline().split(",")# reading the first line in text file and putting elements seperated by "," into list1
list2=f1.readline().split(",")#reading the second line and putting the contents in list2
n1=int(list1[4]) #converting the element present at 4th index of list1 to integer
n2=int(list2[4])#converting the element present at 4th index of list2 to integer
item1=np.array([n1,n2])# putting n1 and n2 in array item1
print(item1)#printing item1
