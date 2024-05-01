import pandas as pd
pd.options.display.max_rows=999
var=pd.read_csv('data.csv')
print(var)
print()
print(var.to_string())
print(pd.options.display.max_rows)
