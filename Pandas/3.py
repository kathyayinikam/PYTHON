import pandas as pd
data={
    'Fruits':["Apple","Mango","Banana","Grapes"],
    'Price/Kg':[200,150,50,70]
    }
var=pd.DataFrame(data)
print(var)
print()
print(var.loc[1])
print()
print(var.loc[[1,2]])
