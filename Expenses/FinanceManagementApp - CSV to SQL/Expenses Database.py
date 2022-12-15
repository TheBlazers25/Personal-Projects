import pandas as pd
import mysql.connector

# Import CSV
data = pd.read_csv(r'dsk_july.csv', usecols=[0, 3, 9], skiprows=[11])
df = pd.DataFrame(data)
df.columns =['Date', 'Name', 'Amount']

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="am336699bs",
  database="expenses"
)

# Create table
if mydb.is_connected():
    mycursor = mydb.cursor()
    mycursor.execute('DROP TABLE IF EXISTS july_expenses;')
    print('Creating table...')
    mycursor.execute("CREATE TABLE july_expenses (date DATE, description VARCHAR(255), amount FLOAT)")

# Insert information
for i, row in data.iterrows():
    sql = "INSERT INTO july_expenses (date, description, amount) VALUES (%s, %s, %s)"
    mycursor.execute(sql, tuple(row))
    print("Expense inserted")

    mydb.commit()

# mycursor.execute("CREATE DATABASE expenses")
