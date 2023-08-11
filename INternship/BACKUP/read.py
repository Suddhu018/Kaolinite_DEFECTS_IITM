import pandas as pd
line_number = 6
df = pd.read_csv('try.CONFIG', skiprows=line_number-1)
print(df[0:67])

