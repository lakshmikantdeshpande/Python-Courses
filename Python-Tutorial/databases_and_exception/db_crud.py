import MySQLdb

# global variables
HOST = "localhost"
USER = "root"
PASS = "root"
DB = "pythondb"


def connect():
    db = MySQLdb.connect(HOST, USER, PASS, DB)
    return db


def disconnect(db):
    try:
        if db is not None:
            db.close()
            print("Connection has been terminated successfully.")
        else:
            raise Exception("Invalid connection (None encountered)")
    except Exception as msg:
        print(msg)


# Create a table
def create_table(db):
    # connect to the database
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS employee")
    sql = """CREATE TABLE EMPLOYEE (
             FIRST_NAME  CHAR(20) NOT NULL,
             LAST_NAME  CHAR(20),
             AGE INT,  
             SEX CHAR(1),
             INCOME FLOAT )"""
    cursor.execute(sql)
    print ("A fresh table is created")


# Insert data in the table
def insert_data(db):
    cursor = db.cursor()
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
             LAST_NAME, AGE, SEX, INCOME)
             VALUES ('Mac', 'S', 20, 'M', 2000)"""
    try:
        cursor.execute(sql)
        db.commit()
        print("Data has been inserted successfully.")
    except:
        db.rollback()


def read_data(db):
    cursor = db.cursor()
    sql = """SELECT * FROM EMPLOYEE"""
    cursor.execute(sql)

    try:  # like resultset
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # Now print fetched result
            print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % (fname, lname, age, sex, income))
    except:
        print("Failed to fetch the data")


# Main functionality
db = connect()
create_table(db)
insert_data(db)
read_data(db)
disconnect(db)
