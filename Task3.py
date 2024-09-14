import sqlite3
#connect database to sqlite3
connection = sqlite3.connect('example.db')
#create object to deal with the database
cursor = connection.cursor()

cursor.execute('''CREATE TABLE PASSENGERS (ID INTEGER PRIMARY KEY, PROOF VARCHAR, AGE INTEGER, NAME VARCHAR)''')

# Insert data into the 'PASSENGERS' table
cursor.execute("INSERT INTO PASSENGERS (proof, age, name) VALUES ('FLASH Card', 22, 'TEJA')")

cursor.execute("INSERT INTO PASSENGERS (proof, age, name) VALUES ('Passport', 22, 'SAI')")

cursor.execute("INSERT INTO PASSENGERS (proof, age, name) VALUES ('FLASH CARD', 22, 'Rathna')")


#Printing PASSENGERS table rows and coloumns
cursor.execute("SELECT * FROM PASSENGERS")
rows = cursor.fetchall()
for row in rows:
    print(row)
  
# Save (commit) the changes
connection.commit()
#handling errors using (try,except)
try:
  cursor.execute("select * from non_existing_table")
except sqlite3.OperationalError as e:
  print(f"An error occured: {e}")
# Insert data using parameters to prevent SQL injection
cursor.execute("INSERT INTO passengers (proof, age, name) VALUES (?, ?, ?)", ('Flash Card', 29, 'Priya'))
connection.commit()

# Query to check the inserted data
cursor.execute("SELECT * FROM passengers WHERE name = 'Priya'")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Drop the 'passengers' table
cursor.execute("DROP TABLE passengers")
try: 
  cursor.execute("SELECT * FROM passengers")
except sqlite3.OperationalError as e:    
  print(f"Error: {e}")
# Close the connection
connection.close()

  


