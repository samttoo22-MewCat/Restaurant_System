import pymysql
import datetime
import cookUI as CUI
import tkinter as tk

class staffUI():
    def __init__(self, user_id):
        self.db = pymysql.connect(host='localhost',
            user='root',
            password='910925As',
            database='test')
        self.cursor = self.db.cursor()
        self.user_id = str(user_id)
    
    def calWorkingMins(self):
        self.cursor.execute("SELECT * FROM clock WHERE user_id = %s and act = 'in'" % (self.user_id))
        results = self.cursor.fetchall()
        last_in = results[len(results) - 1]
        last_in = last_in[len(last_in) - 1]
        last_in = last_in.split(" ")

        last_in_date = last_in[0].split("-")
        last_in_time = last_in[1].split(":")
        last_in_dt = datetime.datetime(int(last_in_date[0]), int(last_in_date[1]), int(last_in_date[2]), int(last_in_time[0]), int(last_in_time[1]), int(last_in_time[2])) 
        

        self.cursor.execute("SELECT * FROM clock WHERE user_id = %s and act = 'out'" % (self.user_id))
        results = self.cursor.fetchall()
        last_out = results[len(results) - 1]
        last_out = last_out[len(last_out) - 1]
        last_out = last_out.split(" ")
        
        last_out_date = last_out[0].split("-")
        last_out_time = last_out[1].split(":")
        last_out_dt = datetime.datetime(int(last_out_date[0]), int(last_out_date[1]), int(last_out_date[2]), int(last_out_time[0]), int(last_out_time[1]), int(last_out_time[2])) 

        tdelta = last_out_dt - last_in_dt
        working_mins = int(tdelta.total_seconds() / 60)
        return(working_mins)
    
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
            self.cursor.execute("update members set work_mins = '%d' where user_id = '%s'" % (newWorkingMins, self.user_id))

            self.db.commit()
            print("Clocked out at %s, total working mins: %d" % (current_time, self.calWorkingMins()))
            
        else:
            print("You have to clock in first to clock out.")

    def showstaff(self):
        self.cursor.execute("SELECT * FROM members where position = 'staff'")
        results = self.cursor.fetchall()
        print(results)

    def showMenu(self):
        self.cursor.execute("SELECT * FROM menu where m_type = '開胃菜'")
        results = self.cursor.fetchall()
        for result in results:
            print(result)
        print()

        self.cursor.execute("SELECT * FROM menu where m_type = '沙拉'")
        results = self.cursor.fetchall()
        for result in results:
            print(result)
        print()
        self.cursor.execute("SELECT * FROM menu where m_type = '飲品'")
        results = self.cursor.fetchall()
        for result in results:
            print(result)
        print()
        self.cursor.execute("SELECT * FROM menu where m_type = '義大利麵'")
        results = self.cursor.fetchall()
        for result in results:
            print(result)
        print()
        self.cursor.execute("SELECT * FROM menu where m_type = '披薩'")
        results = self.cursor.fetchall()
        for result in results:
            print(result)
        print()
        self.cursor.execute("SELECT * FROM menu where m_type = '燉飯'")
        results = self.cursor.fetchall()
        for result in results:
            print(result)
        print()

    def showOrder(self, t_number):
        self.cursor.execute("SELECT * FROM orders where table_number = %d" % t_number)
        results = self.cursor.fetchall()
        print(results)

    def addOrder(self, m_name, t_number):
        from datetime import datetime
        current_time = datetime.now()
        current_time = datetime.strftime(current_time, '%Y-%m-%d %H:%M:%S')
        self.cursor.execute("INSERT INTO `test`.`orders` (`time`, `m_name`, `table_number`) VALUES ('%s', '%s', %d)" % (current_time, str(m_name), int(t_number)))
        self.db.commit()
        CUI.cUI.updatePrepareList()
    def removeOrder(self, m_name, t_number):
        index = CUI.cUI.prepareListbox.get(0, tk.END).index(m_name)
        CUI.cUI.prepareListbox.delete()

    def changeTableState(self, table_number, state):
        self.cursor.execute("UPDATE r_table set state = '%s' where table_number = %d" % (str(state), int(table_number)))
        self.db.commit()
    def getTableState(self):
        self.cursor.execute("SELECT * FROM r_table")
        results = self.cursor.fetchall()
        for result in results:
            state = str(result[0])
            table_number = int(result[1])
            print("Table %d - %s", (table_number, state))

sUI = staffUI("samttoo22")
sUI.addOrder("奶油蔬菜義大利麵", 1)
sUI.addOrder("冰紅茶", 1)
CUI.cUI.open()




