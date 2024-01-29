import mysql.connector as sql
connection = sql.connect(host = 'localhost',
            user = 'root',
            password = '1234',
            database = 'advisors')

cursor = connection.cursor()
cursor.execute("CREATE DATABASE crm")

print("All Done!")