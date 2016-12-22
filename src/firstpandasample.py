#!/usr/bin/python

import pandas as pd

df = pd.DataFrame({'int_col' : [1,2,6,8,-1], 'float_col' : [0.1, 0.2,0.2,10.1,None], 'str_col' : ['a','b',None,'c','a']})
df.index = ["A", "B", "C", "D", "E"]

print df

df2 = df.ix[:,["int_col", "str_col"]] # You can access using df[["int_col", "str_col"]]

df2.loc["A", "int_col"] = 20
print df2

df.ix[:,["int_col", "str_col"]] = df2
print df

print df[df['float_col'] == 0.2][["int_col"]]

print df.T

writer = pd.ExcelWriter("testoutput.xlsx")
df.to_excel(writer)
writer.save()