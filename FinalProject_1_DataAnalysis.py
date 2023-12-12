import pandas as pd
import sqlite3
import matplotlib.pyplot as plt 

DATABASE = 'database.db'
conn = sqlite3.connect(DATABASE)


df = pd.read_sql_query("SELECT * FROM data", conn)
print(df)
df.plot(x='time', y='factor', kind='scatter')	
df.plot(x='time', y='pi', kind='scatter')	
df["factor_cube_rooted"] = (df['factor'] ** (1. / 3))
df.plot(x='time', y='factor_cube_rooted', kind='scatter')	
plt.show()

