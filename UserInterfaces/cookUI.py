import pymysql
from datetime import datetime
import staffUI as SUI

class cookUI():
    def __init__(self, user_id):
        self.db = pymysql.connect(host='localhost',
            user='root',
            password='910925As',
            database='test')
        self.cursor = self.db.cursor()
        self.user_id = str(user_id)
        self.prepareList = []
        

    def isWorking(self):
        
        self.cursor.execute("SELECT * FROM clock WHERE user_id = %s", (self.user_id))
        results = self.cursor.fetchall()
        results = results[len(results) - 1]
        latest = results[1]
        if(latest == "in"):
            return True
        else:
            return False 

    def clockIn(self):
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        if(self.isWorking()):
            print("You have already clocked in, you can't clock in twice!")
        else:  
            self.cursor.execute("INSERT INTO `test`.`clock` (`user_id`, `act`, `clocktime`) VALUES ('%s', '%s', '%s')" % (str(self.user_id), "in", current_time))
            self.db.commit()
            print("Clocked in at %s" % current_time)
        
    def clockOut(self):
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        if(self.isWorking()):
            
            self.cursor.execute("INSERT INTO `test`.`clock` (`user_id`, `act`, `clocktime`) VALUES ('%s', '%s', '%s')" % (str(self.user_id), "out", current_time))
            
            self.cursor.execute("select * from members where user_id = '%s'" % self.user_id)
            results = self.cursor.fetchall()
            currentWorkingMins = results[0][3]
            newWorkingMins = currentWorkingMins + self.calWorkingMins()
            self.cursor.execute("update members set work_mins = '%d' where user_id = '%s'", newWorkingMins, self.user_id)

            self.db.commit()
            print("Clocked out at %s, total working mins: %d" % current_time, self.calWorkingMins())
            
        else:
            print("You have to clock in first to clock out.")

    def show(self):
        self.cursor.execute("SELECT * FROM clock")
        results = self.cursor.fetchall()
        print(results)
        print()

    def removeOrder(self, m_name, t_number):
        self.cursor.execute("SELECT count(*) FROM orders WHERE m_name = '%s' and table_number = %d" % (str(m_name), int(t_number)))
        number = self.cursor.fetchall()
        number = number[0][0]
        if(number > 1):
            self.cursor.execute("SELECT * FROM orders WHERE m_name = '%s' and table_number = %d" % (str(m_name), int(t_number)))
            results = self.cursor.fetchall()
            last_time = results[len(results) - 1][0]
            self.cursor.execute("DELETE FROM orders WHERE time = %d and m_name = '%s' and table_number = %d" % (last_time, str(m_name), int(t_number)))
            self.db.commit()
        else:
            self.cursor.execute("DELETE FROM orders WHERE m_name = '%s' and table_number = %d" % (str(m_name), int(t_number)))
            self.db.commit()

    def updatePrepareList(self):
        self.cursor.execute("SELECT * FROM orders")
        results = self.cursor.fetchall()
        first = []
        second = []
        third = []
        for result in results:
            m_name = result[1]
            t_number = result[2]
            self.cursor.execute("SELECT m_type FROM menu where m_name = '%s'" % m_name)
            m_type = self.cursor.fetchone()
            m_type = m_type[0]
            if(m_type == '開胃菜' or m_type == '沙拉'):
                first.append("%s-%d" % (m_name, t_number))
                self.removeOrder(m_name, t_number)
            elif(m_type == '飲品'):
                second.append("%s-%d" % (m_name, t_number))
                self.removeOrder(m_name, t_number)
            else:
                #主菜類
                third.append("%s-%d" % (m_name, t_number))
                self.removeOrder(m_name, t_number)
        for i in range(0, len(first)):
            self.prepareList.append(first[i])
        for i in range(0, len(second)):
            self.prepareList.append(second[i])
        for i in range(0, len(third)):
            self.prepareList.append(third[i])
            

    def finPrepare(self, m_name, t_number):
        thestr = "%s-%d" % (m_name, t_number)
        del(self.prepareList[self.prepareList.index(thestr)])

    def showPrepareList(self, length):
        if(len(self.prepareList) < length):
            for i in range(0, len(self.prepareList)):
                print(self.prepareList[i])
            print()
        else:
            for i in range(0, length):
                print(self.prepareList[i])
            print()

cUI = cookUI("samttoo22")

cUI.showPrepareList(10)

