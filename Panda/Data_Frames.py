import pandas as pd
calories= {"day1": 350, "day2": 475, "day3": 520}
my_var = pd.Series(calories)
print(my_var)

data = {
    "calories": [350, 475, 520],
    "duration": [35, 55, 60]
}
# load data into a DataFrame object:
df = pd.DataFrame(data)
print(df.loc[0])
print(df.loc[[0, 1]])


# named index
dd = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(dd)
