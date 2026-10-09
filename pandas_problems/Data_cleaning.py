# define a dictionary with sample data which includes some missing values
import pandas as pd
data = {
    "A": [1, 2, 3, None, 5],
    "B": [None, 2, 3, 4, 5],
    "c": [1,2,None,None,5]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n",  df)
print()

# use dropna() to remove rows with missing values
df_cleaned = df.dropna()
print("DataFrame after dropping rows with missing values:\n", df_cleaned)

# fill missing values with a specific value (e.g., 0)
df_filled = df.fillna(0)
print("DataFrame after filling missing values with 0:\n", df_filled)

# fill missing values with the mean of each column
df_filled_mean = df.fillna(df.mean(), inplace=True)
print("DataFrame after filling missing values with column means:\n", df_filled_mean)



