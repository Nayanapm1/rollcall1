import pymysql

db=pymysql.connect('localhost','root','Nay@atharv89','rollcalldb')

cursor=db.cursor()
cursor.execute('select version()')
data=cursor.fetchone()

print("Database version:%s"%data)

cursor.close()
db.close()