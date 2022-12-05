import pymysql


class verifyUI():
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
            user='root',
            password='910925As',
            database='test')
        self.cursor = self.db.cursor()
        self.postion = ""

    def verify(self, username, password):
        self.cursor.execute("SELECT * FROM members")
        results = self.cursor.fetchall()

        for row in results:
            db_username = row[0]
            db_password = row[2]

            if str(username) == db_username and str(password) == db_password:
                self.postion = row[1]
                return True
            else:
                pass
        return False
    

vUI = verifyUI()
if(vUI.verify("samttoo22", 999999)):
    vUI.destroy()
    