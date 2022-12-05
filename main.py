import pymysql
db = pymysql.connect(host='localhost',
                    user='root',
                    password='910925As',
                    database='test')
cursor = db.cursor()
sql = "SELECT * FROM members"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    print(row)
db.close()