import pymssql

conn = pymssql.connect('localhost', 'SA', 'RootRoot5@', 'tempdb')
cursor = conn.cursor()
cursor.execute('SELECT * from sys.databases')

for row in cursor:
    print('row = %r' % (row,))

conn.close()
