import pymysql
from datetime import datetime

class receptionUI():
    def __init__(self, user_id):
        self.db = pymysql.connect(host='localhost',
            user='root',
            password='910925As',
            database='test')
        self.cursor = self.db.cursor()
        self.user_id = str(user_id)

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