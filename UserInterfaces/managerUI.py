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

    def addDish(self, m_type, m_name, m_price):
        try:
            self.cursor.execute("insert `test`.`menu` (`m_type`, `m_name`, `m_price`) VALUES ('%s', '%s', %f);" % (str(m_type), str(m_name), float(m_price)))
            self.db.commit()
        except:
            pass   
    def removeDish(self, m_name):
        try:
            self.cursor.execute("DELETE FROM menu WHERE m_name = '%d'" % (str(m_name)))
            self.db.commit()
        except:
            pass
    
    def addTable(self):
        self.cursor.execute("insert `test`.`r_table` (`state`) values ('clean');")
        self.db.commit()
    def removeTable(self):
        self.cursor.execute("DELETE FROM MARKS WHERE ID = (SELECT MAX(table_number) FROM MARKS)")
        self.db.commit()
mUI = managerUI("samttoo22")

mUI.addTable()
mUI.addTable()
    