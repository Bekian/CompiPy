import pandas as pd
import time
# this code sets up the csv files for data comparison tests
data1 = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
data2 = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 354, 35],
    'City': ['New York', 'Los Angeles', 'hicago']
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Export to CSV
df1.to_csv('output1.csv', index=False)
df2.to_csv('output2.csv', index=False)


if __name__ == "__main__":
    print(time.time())
