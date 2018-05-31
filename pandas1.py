import pandas as pd
xyz = {'day' :[1,2,3,4,5,6], 'visited':[12,23,42,11,13,34], 'bounse':[1,4,2,1,4,5]}
# converting a dictionary into a dataframe
df1 = pd.DataFrame(xyz)
df3 = list(xyz.items())

print(df3)
print(df1.head(2))

abc = {'day' :[7,8,9,10,11], 'visited':[22,33,44,41,23,14], 'bounse':[3,5,2,7,4,9]}
df4 = list(abc.items())
x = pd.DataFrame({'day' :[1,2,3,4,5,6], 'visited':[12,23,42,11,13,34], 'bounse':[1,4,2,1,4,5]}, index = [1,2,3,4,5,6])
# df2 = pd.DataFrame(abc)
a = pd.DataFrame({'day' :[1,2,3,4,5,7], 'visited':[22,33,44,41,23,14], 'bounse':[3,5,2,7,4,9]}, index = [7,8,9,10,11,12])

df5 = pd.merge(x,a, on='day')

print(df5)



