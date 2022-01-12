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

import pandas as pd

a = pd.read_csv('data.csv')
print(a.to_string())
print(a)