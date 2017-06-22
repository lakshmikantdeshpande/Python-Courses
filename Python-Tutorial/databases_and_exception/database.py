# simple connection with MySQL database
import pymysql

db = pymysql.connect('localhost', 'root', 'root', 'pythondb')

cursor = db.cursor()

cursor.execute('SELECT VERSION()')

data = cursor.fetchone()

print("Version of the database is %s" % data)

db.close()
