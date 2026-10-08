# create a label using pandas
import pandas as pd
a = [1,2,3]
my_var = pd.Series(a, index = ["x", "y", "z"])
print(my_var)
a1 = pd.Series([10,20,30], index = ["x", "y", "z"], name = "Example series")
print(a1)