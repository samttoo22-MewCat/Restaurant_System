import pymysql
import datetime
import tkinter as tk


class PtUI():
    def __init__(self, user_id, root):
        def clockIn():
            from datetime import datetime
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            if(isWorking()):
                lbl_1 = tk.Label(self.root, text="你已經刷上了，你不能刷上兩次!", font=('微軟正黑體', 12))
                lbl_1.place(x=480,y=100,width=240,height=120)
            else:  
                self.cursor.execute("INSERT INTO `test`.`clock` (`user_id`, `act`, `clocktime`) VALUES ('%s', '%s', '%s')" % (str(self.user_id), "in", current_time))
                self.db.commit()
                lbl_1 = tk.Label(self.root, text="在 %s 成功刷上" % (current_time), font=('微軟正黑體', 12))
                lbl_1.place(x=480,y=100,width=240,height=120)
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
                lbl_1.place(x=480,y=100,width=240,height=120)
            else:
                lbl_1 = tk.Label(self.root, text="你要先刷上才能刷下。", font=('微軟正黑體', 12))
                lbl_1.place(x=480,y=100,width=240,height=120)
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
        def finish():
            selectedPlace = self.uncleanListbox.curselection()
            text = self.uncleanListbox.get(selectedPlace)
            table_number = int(text[8])

            self.uncleanListbox.delete(selectedPlace)
            self.changeTableState(table_number, "空")

        self.db = pymysql.connect(host='localhost',
            user='root',
            password='910925As',
            database='test',
            autocommit=True)
        self.cursor = self.db.cursor()
        self.user_id = str(user_id)
        self.prepareList = []
        self.root = tk.Toplevel(root)
        self.root.title('餐廳系統-雜工介面')

        width=750
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)

        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)
        
        #label set up
        self.lbl_1 = tk.Label(self.root, relief = "ridge")
        self.lbl_1.place(x=20,y=40,width=426,height=447)
        self.lbl_2 = tk.Label(self.root, relief = "ridge")
        self.lbl_2.place(x=460,y=40,width=270,height=447)
        self.lbl_3 = tk.Label(self.root, bg = "yellow", text='未清理桌子桌號', fg='black', font=('微軟正黑體', 15), anchor='center')
        self.lbl_3.place(x=20,y=10,width=426,height=30)
        self.lbl_4 = tk.Label(self.root, bg = "yellow", text='打卡', fg='black', font=('微軟正黑體', 15), anchor='center')
        self.lbl_4.place(x=460,y=10,width=270,height=30)
        self.uncleanListbox = tk.Listbox(self.root, font=('微軟正黑體', 11))
        self.uncleanListbox.place(x=80,y=80,width=300,height=300)

        #button set up
        bt_1 = tk.Button(self.root, text='完成', font=('微軟正黑體', 12), command=finish )
        bt_1.place(x=190,y=440,width=88,height=30)
        bt_2 = tk.Button(self.root, text='刷上', font=('微軟正黑體', 12), command=clockIn)
        bt_2.place(x=478,y=440,width=88,height=30)
        bt_3 = tk.Button(self.root, text='刷下', font=('微軟正黑體', 12), command=clockOut)
        bt_3.place(x=624,y=440,width=88,height=30)

        self.root.after(100, self.updateUncleanedListbox)
        self.root.protocol("WM_DELETE_WINDOW", lambda x = None: self.root.destroy())
    def updateUncleanedListbox(self):
        self.cursor.execute("SELECT table_number FROM r_table where state = '需清潔'")
        newUncleanedListbox = self.cursor.fetchall()
        currentUncleanedListbox = self.uncleanListbox.get(0, tk.END)
        for i in newUncleanedListbox:
            output = "需清潔 - 第 %d 桌" % i
            if(output not in currentUncleanedListbox):
                self.uncleanListbox.insert(tk.END, "需清潔 - 第 %d 桌" % i)
        self.root.after(100, self.updateUncleanedListbox)

    def open(self):
        self.root.mainloop()

    def changeTableState(self, table_number, state):
        self.cursor.execute("UPDATE r_table set state = '%s' where table_number = %d" % (str(state), int(table_number)))
        self.db.commit()
        self.cursor.execute("SELECT * FROM r_table where table_number = %d" % int(table_number))
        result = self.cursor.fetchone()
        state = str(result[0])
        return state
            
