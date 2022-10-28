import pandas as pd
import numpy as np

# pd.set_option('display.max_columns', 70)
# pd.set_option('display.max_rows', None)

df = pd.DataFrame(columns = ["A","B"])

df = pd.DataFrame(index = ["a","b"], columns = ["A","B"])
#      A    B
# a  NaN  NaN
# b  NaN  NaN

df = pd.DataFrame(np.zeros([2,2]), index = ["a","b"], columns = ["A","B"])
#      A    B
# a  0.0  0.0
# b  0.0  0.0

df = pd.DataFrame(np.zeros([2,2]))
c = pd.MultiIndex.from_arrays([["A", ""], ["x","y"]])
df.columns = c
#      A     
#      x    y
# 0  0.0  0.0
# 1  0.0  0.0


for i in range(0,3):
    exec(f"df{i} = df")



a =list(range(0,4))
print(a)
# [0, 1, 2, 3]

a = list(range(0,8,2))
print(a)
# [0, 2, 4, 6]

a = np.reshape(a,(2,2))
print(a)
# [[0 2]
#  [4 6]]

df = pd.DataFrame(a)
