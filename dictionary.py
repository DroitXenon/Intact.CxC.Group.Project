import sqlite3
import pandas as pd

# Connect to the SQLite database
sql_connect = sqlite3.connect('intact.db')
cursor = sql_connect.cursor()

# Create a string of column names separated by commas
words_space = ""
for i in range(20):
    words_space = words_space + "word" + str(i) + ", "
columns = "(Idx, " + words_space + "Label);"

# Create a temporary table with the specified columns
create = "CREATE TEMP TABLE Dictionary" + columns
cursor.execute(create)

# Execute a query to select all the rows from the temporary table
query = "SELECT * FROM Dictionary;"
db_df = pd.read_sql_query(query, sql_connect)

# Export the DataFrame to a CSV file without including the index
db_df.to_csv('database.csv', index=False)