import mysql.connector
import qry

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="kannan$7500",
  database="mydatabase"
)

mycursor = db.cursor()
mycursor.execute(qry.create_tbl)
