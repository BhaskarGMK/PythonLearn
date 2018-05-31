import pandas as pd
import matplotlib.pyplot as mp
from matplotlib import style
style.use("fivethirtyeight")
# this is about joining
x = pd.DataFrame({'visited':[12,23,42,11,13,34], 'bounse':[1,4,2,1,4,5], 'us':[12,23,34,12,22,45]}, index = [1,2,3,4,5,6])
# df2 = pd.DataFrame(abc)
a = pd.DataFrame({'visited':[22,33,44,41,23,14], 'bounse':[3,5,2,7,4,9], 'india':[12,23,34,12,22,45]}, index = [7,8,9,10,11,12])
'''
joining = a.join(x)

# print(joining)

df1 = pd.DataFrame({'casino':[1,2,3,4,5], 'visit':[20,40,50,24,35], 'left':[5,2,3,5,6]})
df1.set_index('casino', inplace=True)
print(df1)

df1.plot()
mp.show()
df1 = df1.rename(columns = {"visit":"biscuits"})
print(df1)


concat = pd.concat([x,a], sort=True)
print(concat)
'''

honey = pd.read_csv('honeyproduction.csv', index_col=0)
print(honey)
honey.to_html('honey.html')
