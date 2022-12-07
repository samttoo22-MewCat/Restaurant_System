import pymysql
db = pymysql.connect(host='localhost',
                    user='root',
                    password='910925As',
                    database='test')
cursor = db.cursor()
sql = "SELECT * FROM menu WHERE m_type = '飲品'"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    print(row)
db.close()