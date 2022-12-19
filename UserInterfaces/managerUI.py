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
        self.cursor.execute("INSERT INTO `test`.`members` (`user_id`, `user_password`, `position`, `work_mins`) VALUES ('%s', '%s', '%s', '%d')" % (str(username), str(password), str(position), 0))
        self.db.commit()
        
    def removeMember(self, username):
        self.cursor.execute("DELETE FROM members WHERE user_id = '%s'" % str(username))
        self.db.commit()
        

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
        self.cursor.execute("select table_number from r_table")
        
        table_number = self.cursor.fetchall()    
        last_table_number = table_number[len(table_number) - 1][0]

        self.cursor.execute("insert `test`.`r_table` (`state`, `tableorderList`, `table_number`) values ('空', '', %d);" % (last_table_number + 1))
        self.db.commit()
    def removeTable(self):
        self.cursor.execute("select table_number from r_table")
        table_number = self.cursor.fetchall()
        table_number = table_number[0]
        
        last_table_number = table_number[len(table_number) - 1]
        if(last_table_number > 0):
            self.cursor.execute("SELECT MAX(table_number) FROM r_table")
            table_number = self.cursor.fetchone()
            table_number = table_number[0]

            self.cursor.execute("DELETE FROM r_table WHERE table_number = %d" % table_number)
            self.db.commit()
mUI = managerUI("samttoo22")

mUI.addMember("cook", "cook01", "999999")