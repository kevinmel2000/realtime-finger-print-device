from peewee import *
from models.database import mysql_db

class Attendance_Logs(Model):
    user_id     = IntegerField()
    time        = CharField()

    class Meta:
        database = mysql_db