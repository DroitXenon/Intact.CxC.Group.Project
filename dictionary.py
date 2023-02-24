import sqlite3
import pandas as pd

# Connect to the SQLite database
sql_connect = sqlite3.connect('intact.db')
cursor = sql_connect.cursor()

# Create a string that represent commas seperated column names 
words_space = ""
for i in range(100):
  words_space += most_occur[i][0] + "_, "

# Generate a string that reflect the structure of the Table
columns = "(" + words_space + "Label);"

# Create the Table
create = "CREATE TEMP TABLE Dictionary" + columns
cursor.execute(create)

# For each label, create a row for it 
for i in range(40):
  # Cast the frequency dict for the ith label to a list 
  lst = list(ls_dict[i].keys())
  # Declare a string to store the values used in insertion
  values_to_insert = "("
  for j in range(100):
    # For each of the top 100 frequent words, attach the count for ith label as a value to insert
    label_dict = ls_dict[i]
    values_to_insert += str(label_dict[lst[j]]) + ", "
  values_to_insert += str(i) + ");"
  
  # Insert the row into Dictionary
  insert = "INSERT INTO Dictionary (" + words_space + "Label) VALUES " + values_to_insert
  cursor.execute(insert)

# Select all entries from Dictionary
query = "SELECT * FROM Dictionary;"
results = cursor.execute(query).fetchall()
pd.read_sql_query(query,sql_connect)

# Export the DataFrame to a CSV file without including the index
db_df = pd.read_sql_query(query, sql_connect)
db_df.to_csv('database.csv', index=True)
