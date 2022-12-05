import pymysql
import datetime

class staffUI():
    def __init__(self, user_id):
        self.db = pymysql.connect(host='localhost',
            user='root',
            password='910925As',
            database='test')
        self.cursor = self.db.cursor()
        self.user_id = str(user_id)
    
    def calWorkingMins(self):
        self.cursor.execute("SELECT * FROM clock WHERE user_id = %s and act = 'in'", (self.user_id))
        results = self.cursor.fetchall()
        last_in = results[len(results) - 1]
        last_in = last_in[len(last_in) - 1]
        last_in = last_in.split(" ")

        last_in_date = last_in[0].split("-")
        last_in_time = last_in[1].split(":")
        last_in_dt = datetime.datetime(int(last_in_date[0]), int(last_in_date[1]), int(last_in_date[2]), int(last_in_time[0]), int(last_in_time[1]), int(last_in_time[2])) 
        

        self.cursor.execute("SELECT * FROM clock WHERE user_id = %s and act = 'out'", (self.user_id))
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

    def show(self):
        self.cursor.execute("SELECT * FROM clock")
        results = self.cursor.fetchall()
        print(results)


sUI = staffUI("samttoo22")

sUI.show()
sUI.clockOut()

