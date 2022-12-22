import pymysql
import datetime
import tkinter as tk

class managerUI():
    def __init__(self, user_id):
        def clockIn():
            from datetime import datetime
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            if(isWorking()):
                lbl_1 = tk.Label(self.root, text="你已經刷上了，你不能刷上兩次!", font=('微軟正黑體', 12))
                lbl_1.place(x=170,y=310,width=263,height=162)
            else:  
                self.cursor.execute("INSERT INTO `test`.`clock` (`user_id`, `act`, `clocktime`) VALUES ('%s', '%s', '%s')" % (str(self.user_id), "in", current_time))
                self.db.commit()
                lbl_1 = tk.Label(self.root, text="在 %s 成功刷上" % (current_time), font=('微軟正黑體', 12))
                lbl_1.place(x=170,y=310,width=263,height=162)
        def clockOut():
            from datetime import datetime
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            if(isWorking()):
                self.cursor.execute("INSERT INTO `test`.`clock` (`user_id`, `act`, `clocktime`) VALUES ('%s', '%s', '%s')" % (str(self.user_id), "out", current_time))
                self.cursor.execute("select * from members where user_id = '%s'" % self.user_id)
                results = self.cursor.fetchall()
                currentWorkingMins = results[0][3]
                newWorkingMins = currentWorkingMins + calWorkingMins()
                self.cursor.execute("update members set work_mins = '%d' where user_id = '%s'" % (newWorkingMins, self.user_id))

                self.db.commit()
                lbl_1 = tk.Label(self.root, text="在 %s 成功刷下,\n 此次總工時: %d 分 %d 秒" % (current_time, int(calWorkingMins() // 60),  int(calWorkingMins() % 60)), font=('微軟正黑體', 12))
                lbl_1.place(x=170,y=310,width=263,height=162)
            else:
                lbl_1 = tk.Label(self.root, text="你要先刷上才能刷下。", font=('微軟正黑體', 12))
                lbl_1.place(x=170,y=310,width=263,height=162)
        def isWorking():
            self.cursor.execute("SELECT * FROM clock WHERE user_id = %s", (self.user_id))
            results = self.cursor.fetchall()
            results = results[len(results) - 1]
            latest = results[1]
            if(latest == "in"):
                return True
            else:
                return False 
        def calWorkingMins():
            self.cursor.execute("SELECT * FROM clock WHERE user_id = '%s' and act = 'in'" % (self.user_id))
            results = self.cursor.fetchall()
            last_in = results[len(results) - 1]
            last_in = last_in[len(last_in) - 1]
            last_in = last_in.split(" ")

            last_in_date = last_in[0].split("-")
            last_in_time = last_in[1].split(":")
            last_in_dt = datetime.datetime(int(last_in_date[0]), int(last_in_date[1]), int(last_in_date[2]), int(last_in_time[0]), int(last_in_time[1]), int(last_in_time[2])) 
            

            self.cursor.execute("SELECT * FROM clock WHERE user_id = '%s' and act = 'out'" % (self.user_id))
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
        def addTable():
            self.cursor.execute("select table_number from r_table")
        
            table_number = self.cursor.fetchall()    
            last_table_number = table_number[len(table_number) - 1][0]

            self.cursor.execute("insert `test`.`r_table` (`state`, `tableorderList`, `table_number`) values ('空', '', %d);" % (last_table_number + 1))
            self.db.commit()
            self.lbl_1 = tk.Label(self.root, text="已成功新增桌子，目前共有 %d 張桌子" % (last_table_number + 1), font=('微軟正黑體', 12))
            self.lbl_1.place(x=170,y=310,width=263,height=162)
        def removeTable():
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
                self.lbl_1 = tk.Label(self.root, text="已成功刪除桌子，目前共有 %d 張桌子" % (table_number - 1), font=('微軟正黑體', 12))
                self.lbl_1.place(x=170,y=310,width=263,height=162)
            else:
                self.lbl_1 = tk.Label(self.root, text="錯誤: 已經沒有桌子了。", font=('微軟正黑體', 12))
                self.lbl_1.place(x=170,y=310,width=263,height=162)
        def addMember(position, username, password):
            if(thisPositionExist(position)):
                self.cursor.execute("INSERT INTO `test`.`members` (`user_id`, `user_password`, `position`, `work_mins`) VALUES ('%s', '%s', '%s', '%d')" % (str(username), str(password), str(position), 0))
                self.db.commit()
                self.lbl_1 = tk.Label(self.root, text="已成功新增員工 - \n職位: %s, \n帳號: %s, \n密碼: %s" % (position, username, password), font=('微軟正黑體', 12))
                self.lbl_1.place(x=170,y=310,width=263,height=162)
            else:
                self.lbl_1 = tk.Label(self.root, text="此職位不存在，請重試。")
                self.lbl_1.place(x=170,y=310,width=263,height=162)
        def removeMember(username):
            self.cursor.execute("DELETE FROM members WHERE user_id = '%s'" % str(username))
            self.db.commit()
            self.lbl_1 = tk.Label(self.root, text="已成功刪除員工帳號: %s" % (username), font=('微軟正黑體', 12))
            self.lbl_1.place(x=170,y=310,width=263,height=162)
        
        def thisPositionExist(postion):
            if(postion == "manager" or postion == "staff" or postion == "PTworker" or postion == "reception" or postion == "staff"):
                return True
            else:
                return False

        self.db = pymysql.connect(host='localhost',
            user='root',
            password='910925As',
            database='test')
        self.cursor = self.db.cursor()
        self.user_id = str(user_id)
        self.root = tk.Tk()
        #setting title
        self.root.title("餐廳系統-經理介面")
        #setting window size
        self.width=649
        self.height=504
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        self.alignstr = '%dx%d+%d+%d' % (self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)
        self.root.geometry(self.alignstr)
        self.root.resizable(width=False, height=False)

        self.GButton_926=tk.Button(self.root, bg="#009688", font=('微軟正黑體', 10), justify="center", text="增加桌子數量", command=addTable)
        self.GButton_926.place(x=10,y=10,width=144,height=30)

        self.GButton_802=tk.Button(self.root, bg="#5fb878", font=('微軟正黑體', 10), fg="#000000", justify="center", text="減少桌子數量", command=removeTable)
        self.GButton_802.place(x=170,y=10,width=144,height=30)

        self.GButton_840=tk.Button(self.root, bg="#1e9fff", font=('微軟正黑體', 10), fg="#000000", justify="center", text="增加工作人員", command= lambda: addMember(username=self.GLineEdit_248.get(), password=self.GLineEdit_257.get(), position=self.GLineEdit_949.get()))
        self.GButton_840.place(x=10,y=50,width=144,height=30)

        self.GButton_840=tk.Button(self.root, bg="#1e9fff", font=('微軟正黑體', 10), fg="#000000", justify="center", text="顯示工作人員名單")
        self.GButton_840.place(x=170,y=50,width=144,height=30)

        self.GButton_972=tk.Button(self.root, bg="#1e9fff", font=('微軟正黑體', 10), fg="#000000", justify="center", text="刪除工作人員", command= lambda: removeMember(username=self.GLineEdit_295.get()))
        self.GButton_972.place(x=10,y=210,width=144,height=30)

        self.GButton_29=tk.Button(self.root, bg="#00babd", font=('微軟正黑體', 10), fg="#000000", justify="center", text="查看員工效率")
        self.GButton_29.place(x=360,y=170,width=144,height=30)

        self.GButton_774=tk.Button(self.root, bg="#00babd", font=('微軟正黑體', 10), fg="#000000", justify="center", text="查看工資列表")
        self.GButton_774.place(x=360,y=90,width=144,height=30)

        self.GButton_936=tk.Button(self.root, bg="#00babd", font=('微軟正黑體', 10), fg="#000000", justify="center", text="查看盈餘狀況")
        self.GButton_936.place(x=360,y=130,width=143,height=30)

        self.GButton_91=tk.Button(self.root, bg="#c71585", font=('微軟正黑體', 10), fg="#000000", justify="center", text="刷下", command=clockIn)
        self.GButton_91.place(x=10,y=350,width=144,height=30)
        
        self.GButton_335=tk.Button(self.root, bg="#c71585", font=('微軟正黑體', 10), fg="#000000", justify="center", text="刷上", command=clockOut)
        self.GButton_335.place(x=10,y=310,width=145,height=30)

        self.GLabel_153=tk.Label(self.root, bg="#ffb800", font=('微軟正黑體', 10), fg="#333333", justify="center", text="帳號")
        self.GLabel_153.place(x=10,y=90,width=71,height=30)

        self.GLabel_831=tk.Label(self.root, bg="#ffb800", font=('微軟正黑體', 10), fg="#333333", justify="center", text="密碼")
        self.GLabel_831.place(x=10,y=130,width=70,height=30)

        self.GLabel_717=tk.Label(self.root, bg="#ffb800", font=('微軟正黑體', 10), fg="#333333", justify="center", text="職位")
        self.GLabel_717.place(x=10,y=170,width=70,height=30)

        self.GLabel_653=tk.Label(self.root, bg="#ffb800", font=('微軟正黑體', 10), fg="#333333", justify="center", text="帳號")
        self.GLabel_653.place(x=10,y=250,width=70,height=30)

        self.GLineEdit_248=tk.Entry(self.root, borderwidth="1px", font=('微軟正黑體', 10), fg="#333333", justify="left")
        self.GLineEdit_248.place(x=80,y=90,width=181,height=30)

        self.GLineEdit_257=tk.Entry(self.root, borderwidth="1px", font=('微軟正黑體', 10), fg="#333333", justify="left")
        self.GLineEdit_257.place(x=80,y=130,width=181,height=30)

        self.GLineEdit_949=tk.Entry(self.root, borderwidth="1px", font=('微軟正黑體', 10), fg="#333333", justify="left")
        self.GLineEdit_949.place(x=80,y=170,width=181,height=30)

        self.GLineEdit_295=tk.Entry(self.root, borderwidth="1px", font=('微軟正黑體', 10), fg="#333333", justify="left")
        self.GLineEdit_295.place(x=80,y=250,width=182,height=30)

        
    


    
        

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
    
    
    def open(self):
            self.root.mainloop()

mUI = managerUI("samttoo22")
mUI.open()