import sys, os
sys.path.append(os.path.abspath('./config'))

import config
import mysql.connector
from flask_restful import Resource

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="kannan$7500",
    database="mydatabase"
    )

