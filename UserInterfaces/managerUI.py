import pymysql
from datetime import datetime

class managerUI():
    def __init__(self, user_id):
        self.db = pymysql.connect(host='localhost',
            user='root',
            password='910925As',
            database='test')
        self.cursor = self.db.cursor()
        self.user_id = str(user_id)


    def addMember(self, position, username, password):
        try:
            self.cursor.execute("INSERT INTO `test`.`members` (`user_id`, `user_password`, `position`, `work_mins`) VALUES ('%s', '%s', '%s', '%d')" % (str(username), str(password), str(position)), 0)
            self.db.commit()
        except:
            pass
    def removeMember(self, username):
        try:
            self.cursor.execute("DELETE FROM members WHERE user_id = '%s'" % str(username))
            self.db.commit()
        except:
            pass

mUI = managerUI()

mUI.cursor.execute("SELECT * FROM members")
results = mUI.cursor.fetchall()
print(results)
    