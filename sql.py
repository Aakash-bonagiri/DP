#pip install mysql-connector-python
"""
CREATE DATABASE STUDENTDATA;

USE STUDENTDATA;

CREATE TABLE STUDENT(
ROLLNO INT,
NAME VARCHAR(100),
AGE INT
);

INSERT INTO STUDENT(ROLLNO, NAME, AGE) VALUES
(1, 'AAKASH', 23),
(2, 'ALICE', 22),
(3, 'BOB', 21);

SELECT * FROM STUDENT;
"""
import mysql.connector

# Establish connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",       # or your database server IP/domain
    user="root",   # your MySQL username
    password="root", # your MySQL password
    database="STUDENTDATA"  # name of the database you want to connect to
)

# Check if the connection is successful
if conn.is_connected():
    print("Connected to MySQL database")
    cursor = conn.cursor()

    # Step 3: Execute SQL query
    cursor.execute("SELECT * FROM student")

    # Step 4: Fetch all rows
    rows = cursor.fetchall()

    #C:\Users\AAKASH BONAGIRI\OneDrive\Desktop\ML\lab\sql.py

    # Step 5: Print the results
    print("Student Table Data: (ROLLNO, NAME, AGE)")
    for row in rows:
        print(row)

# Close the connection
conn.close()
