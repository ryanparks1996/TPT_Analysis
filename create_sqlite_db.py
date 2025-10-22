import sqlite3
import pandas as pd

# Load data file
df = pd.read_csv("C:/Users/ryans/Documents/TPT Project/Copy of Average TPT.csv")

# Create SQLite dataabase
connection = sqlite3.connect('C:/Users/ryans/Documents/TPT Project/TPT.db')

# Load data file to database
df.to_sql('weekly_tpt', connection, if_exists='replace')

# Close connection
connection.close()