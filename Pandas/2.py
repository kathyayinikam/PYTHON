import pandas as pd
alphabets={"A":65,"B":66,"C":67,"D":68}
var=pd.Series(alphabets)
var2=pd.Series(alphabets,index=["A","B"])
print(var)
print(var2)
