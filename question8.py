# Pandas DataFrame with Computed Column
import pandas as pd  # Using pandas
#1. The data given in the assignment
data = {"A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]}
#2. Turn the dictionary into a DataFrame
#Basically this creates a table so it's easier to work with
df = pd.DataFrame(data)
#3. Add a new column based on the existing ones
#Just a simple example: treating A as quantity and B as price
df["Total"] = df["A"] * df["B"]
#4. Print the final table to see the result
print("DataFrame after adding the new column:")
print(df)
