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

def read(qry, val=None):
    try:
        cursor = db.cursor()
        if val == None:
            cursor.execute(qry)
        else:
            cursor.execute(qry, val)
        result = cursor.fetchall()
        count = cursor.rowcount
        print(count)
        if count > 0:
            print(result)
        else:
            print([])
        # for x in result:
        #     print(x[0])

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if (db.is_connected()):
            cursor.close()
            # db.close()

