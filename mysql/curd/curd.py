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

if db.is_connected():
    db_Info = db.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = db.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)

# to execute insert query
def modifi(qry, val=None):
    try:
        cursor = db.cursor()
        if val == None:
            cursor.execute(qry)
        else:
            cursor.execute(qry, val)
        row_headers=[x[0] for x in cur.description]
        db.commit()
        count = cursor.rowcount
        print(count)
        return count
    except Error as e:
        print("Error while connecting to MySQL", e)
        db.rollback()
        return 0
    finally:
        if(db.is_connected()):
            cursor.close()
            # db.close()


# to execute select query
def read(qry, val=None):
    try:
        cursor = db.cursor()
        if val == None:
            cursor.execute(qry)
        else:
            cursor.execute(qry, val)
        rv = cursor.fetchall()
        count = cursor.rowcount
        print(count)
        if count > 0:
            json_data=[]
            row_headers=[x[0] for x in cursor.description]
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            return json_data
        else:
            print([])
            return []
        # for x in result:
        #     print(x[0])

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if (db.is_connected()):
            cursor.close()
            # db.close()

