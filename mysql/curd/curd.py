# import sys, os
# sys.path.append(os.path.abspath('./config'))

# import config
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="mydatabase"
    )

def insert(qry, val):
    cursor = db.cursor()
    cursor.execute(qry)
    db.commit()
    count = cursor.rowcount
    print(count)
    cursor.close()

def read(qry, val):
    try:
        cursor = db.cursor()
        cursor.execute(qry)
        result = cursor.fetchall()
        print(result)
        for x in result:
            print(x[0])

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if (db.is_connected()):
            cursor.close()
            # db.close()

