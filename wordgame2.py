list1 = []
user=[]
var=False
ucount=0
count=0
with open("dictionary.txt", "r") as f1:
    content = f1.readlines()
    list1 = [word.strip() for word in content]
print("Welcome to word game")
print("Enter as long word as possible") 
for i in range(5):
    uword = input("Enter a word: ")
    if uword in user:
             print("This word is already taken")
    else:
            user.append(uword)
            print(user)
            
            ucount=ucount+len(uword)
            b = uword[-1].lower()
            words = [word for word in list1 if b == word[0].lower()]
            if words:
                long_word = max(words, key=len)
                list1.remove(long_word)
               
                count=count+len(long_word)
                print(long_word)  
            else:
                print("Computer runs out of words")
print("Your score=",ucount)
print("Computer score=",count)
if(count>ucount):
        print("Computer wins")
else:
                    
        print("You win")
     
    
