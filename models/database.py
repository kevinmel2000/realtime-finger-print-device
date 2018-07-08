from peewee import *
from config import *

mysql_db = MySQLDatabase(MYSQL_DATABASE, 
                        user=MYSQL_USERNAME, 
                        password=MYSQL_PASSWORD,
                        host=MYSQL_HOST, 
                        port=MYSQL_PORT)

                        
