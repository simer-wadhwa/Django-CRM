import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='simer',

)

#prepare cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE QuestGlobal")

print("ALL Done!")