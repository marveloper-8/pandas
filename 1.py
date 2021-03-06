# import pandas as pd

# a = {
#     'cars': ['BMW', 'Volvo', 'Ford'],
#     'passings': [3, 7, 2]
# }
# b = pd.DataFrame(a)
# print(b)

# print(pd.__version__)

# import pandas as pd
# a = [1, 7, 2]
# b = pd.Series(a)
# print(b)
# print(b[0])

# c = pd.Series(a, index=["x", "y", "z"])
# print(c)
# print(c["y"])

# d = {
#     "day1": 420,
#     "day2": 380,
#     "day3": 390
# }
# e = pd.Series(d)
# print(e)
# f = pd.Series(d, index=["day1", "day2"])
# print(f)

# g = {
#     "h": [420, 380, 390],
#     "i": [50, 40, 45]
# }
# j = pd.DataFrame(g)
# print(j)

# import pandas as pd

# a = {
#     "b": [420, 380, 390],
#     "c": [50, 40, 45]
# }
# d = pd.DataFrame(a)
# print(d)
# print(d.loc[0])
# print(d.loc[[0, 1]])

# e = pd.DataFrame(a, index=["day1", "day2", "day3"])
# print(e)
# print(e.loc["day2"])

# f = pd.read_csv('data.csv')
# print(f)

# import pandas as pd

# a = pd.read_csv('data.csv')
# print(a.to_string())
# print(a)
# print(pd.options.display.max_rows)

# pd.options.display.max_rows = 9999
# b = pd.read_csv('data.csv')
# print(b)

# import pandas as pd

# a = pd.read_json('data.json')
# print(a.to_string())

# b = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }

# c = pd.DataFrame(b)
# print(c)

# import pandas as pd

# a = pd.read_csv('data.csv')
# print(a.head(10))
# print(a.head()) 
# print(a.tail()) 
# print(a.info())

# import pandas as pd

# a = pd.read_csv('dirtydata.csv')

# b = a["Calories"].mode()[0]
# a["Calories"].fillna(b, inplace = True)
# print(a)

# c = a["Calories"].median()
# a["Calories"].fillna(c, inplace = True)
# print(a.to_string())

# b = a.dropna()
# print(b.to_string())

# c = a["Calories"].mean()
# a["Calories"].fillna(c, inplace = True)
# print(a)

# a["Calories"].fillna(130, inplace = True)
# print(a)

# a.fillna(130, inplace = True)
# print(a)

# a.dropna(inplace = True)
# print(a.to_string())

# import pandas as pd

# a = pd.read_csv('dirtydata.csv')
# a['Date'] = pd.to_datetime(a['Date'])
# a.dropna(subset=['Date'], inplace=True)
# print(a.to_string())

# import pandas as pd

# a = pd.read_csv('dirtydata.csv')

# for b in a.index:
#     if a.loc[b, 'Duration'] > 120:
#         a.drop(b, inplace=True)

# print(a.to_string())

# for b in a.index:
#     if a.loc[b, 'Duration'] > 120:
#         a.loc[b, 'Duration'] = 120

# print(a.to_string())

# a.loc[7, 'Duration'] = 45
# print(a.to_string())

# import pandas as pd

# a = pd.read_csv('dirtydata.csv')
# print(a.duplicated())

# a.drop_duplicates(inplace=True)
# print(a.to_string())

# import pandas as pd

# a = pd.read_csv('data1.csv')
# print(a.corr())

import pandas as pd
import matplotlib.pyplot as plt

a = pd.read_csv('data2.csv')
# a.plot(kind='scatter', x='Duration', y='Maxpulse')
a['Duration'].plot(kind='hist')
plt.show()