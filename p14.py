import random
def otp(n1):
    n=n1
    for i in range(0,10,1):
        a=random.randint(10**(n-1),10**n)
        print(a)
banknames=["HDFC","ICICI","CANARA BANK"]
bankname=input("Enter the name of the bank").upper()
if(banknames[0]==bankname):
   print("HDFC OTPs are:")
   otp(6)
else:
    if bankname in banknames:
        print(bankname,"OTP are:")
        otp(8)
    else:
        print(bankname,"not registered")
