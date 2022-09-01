import psycopg2
import sys

#establishing the connection
conn = psycopg2.connect(
    database="music", user='admini', password='Abc123456!', host='music.cluster-czudoftmqjrj.us-east-1.rds.amazonaws.com', port='5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Create Table
# sql = '''CREATE TABLE test(ID INT PRIMARY KEY,Name CHAR(20),AGE INT)'''
# cursor.execute(sql)
# conn.commit()

#Add Data:
# cursor.execute('''INSERT INTO test(ID, Name, AGE) VALUES (1, 'Maor', 27)''')
# cursor.execute('''INSERT INTO test(ID, Name, AGE) VALUES (2, 'niin', 25)''')
# cursor.execute('''INSERT INTO test(ID, Name, AGE) VALUES (3, 'saar', 30)''')
# conn.commit()

cursor.execute('''SELECT * from test''')
result = cursor.fetchall()
print(result)

#Delete Table
# cursor.execute("DROP TABLE POC")
# conn.commit()
