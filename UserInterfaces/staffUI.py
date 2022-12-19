import pymysql
import datetime
import tkinter as tk
from functools import partial

class staffUI():
    def __init__(self, user_id):
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
        self.db = pymysql.connect(host='localhost',
            user='root',
            password='910925As',
            database='test')
        self.cursor = self.db.cursor()
        self.user_id = str(user_id)
        
        self.prepareList = []
        #window set up
        self.root = tk.Tk() 
        self.root.title('餐廳系統-服務員介面')
        self.width=750
        self.height=500
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)
        self.user_id = user_id
        self.tableNumber = 0
    
        #label and button set up
        lbl_1 = tk.Label(self.root, relief = "ridge")
        lbl_1.place(x=20,y=40,width=426,height=447)
        lbl_2 = tk.Label(self.root, relief = "ridge")
        lbl_2.place(x=460,y=40,width=270,height=447)
        lbl_3 = tk.Label(self.root, bg = "yellow", text='餐點準備清單', fg='black', font=('微軟正黑體', 15), anchor='center')
        lbl_3.place(x=20,y=10,width=426,height=30)
        lbl_4 = tk.Label(self.root, bg = "yellow", text='打卡', fg='black', font=('微軟正黑體', 15), anchor='center')
        lbl_4.place(x=460,y=10,width=270,height=30)
       
        
        
        bt_2 = tk.Button(self.root, text='刷上', font=('微軟正黑體', 12), command=clockIn)
        bt_2.place(x=478,y=440,width=88,height=30)
        bt_3 = tk.Button(self.root, text='刷下', font=('微軟正黑體', 12), command=clockOut)
        bt_3.place(x=624,y=440,width=88,height=30)
        self.cursor.execute("select * from r_table")
        r_table_num = len(self.cursor.fetchall())
        for i in range(r_table_num):
            self.addTableMenu()

        #table state
        sets=("空","正在使用","需清潔")

        #change table state
        var1=tk.StringVar(self.root) 
        var1.set("空")

        #show table state
        opm_1=tk.OptionMenu(self.root, var1, *sets)
        opm_1.place(x=180,y=110,width=100,height=35)

    
    def changeList(self, table_number):
        table_number = int(table_number)
        newWindow = tk.Toplevel(self.root)
        newWindow.title('點餐系統')
        width=600
        height=500
        screenwidth = newWindow.winfo_screenwidth()
        screenheight = newWindow.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        newWindow.geometry(alignstr)
        newWindow.resizable(width=False, height=False)
        selectedbox = []
        

        def getMenu():
            self.cursor.execute("SELECT * FROM menu where m_type = '開胃菜'")
            results = self.cursor.fetchall()
            for result in results:
                m_name = result[1]
                menuListbox.insert(tk.END, m_name)

            self.cursor.execute("SELECT * FROM menu where m_type = '沙拉'")
            results = self.cursor.fetchall()
            for result in results:
                m_name = result[1]
                menuListbox.insert(tk.END, m_name)
            self.cursor.execute("SELECT * FROM menu where m_type = '飲品'")
            results = self.cursor.fetchall()
            for result in results:
                m_name = result[1]
                menuListbox.insert(tk.END, m_name)
            self.cursor.execute("SELECT * FROM menu where m_type = '義大利麵'")
            results = self.cursor.fetchall()
            for result in results:
                m_name = result[1]
                menuListbox.insert(tk.END, m_name)
            self.cursor.execute("SELECT * FROM menu where m_type = '披薩'")
            results = self.cursor.fetchall()
            for result in results:
                m_name = result[1]
                menuListbox.insert(tk.END, m_name)
            self.cursor.execute("SELECT * FROM menu where m_type = '燉飯'")
            results = self.cursor.fetchall()
            for result in results:
                m_name = result[1]
                menuListbox.insert(tk.END, m_name)

        
        #delete selected table
        def delete():
            selectedPlace = tableorderListbox.curselection()
            selectedorder = tableorderListbox.get(selectedPlace)

            self.cursor.execute("SELECT tableorderList FROM r_table where table_number = %d" % table_number)
            oldorderList = self.cursor.fetchone()
            oldorderList = oldorderList[0]
            oldorderList = oldorderList.split(" ")
            
            del(oldorderList[oldorderList.index(selectedorder)])
            
            neworderList = ""
            for i in oldorderList:
                
                neworderList = neworderList + " " + i
            print(neworderList)

            self.cursor.execute("UPDATE r_table set tableorderList = '%s' where table_number = %d" % (neworderList, table_number))
            self.db.commit()
            updateSelectedList()

        def updateSelectedList():
            tableorderListbox.delete(0, tk.END)
            self.cursor.execute("SELECT tableorderList FROM r_table where table_number = %d" % table_number)
            results = self.cursor.fetchone()
            results = results[0]
            results = results.split(" ")
            for result in results:
                if(result == ""):
                    pass
                else:
                    tableorderListbox.insert(tk.END, result)

        #menu for adding
        def menuSelect():
            selectedPlace = menuListbox.curselection()
            m_name = menuListbox.get(selectedPlace)
            self.addOrder(m_name)

            self.cursor.execute("SELECT tableorderList FROM r_table where table_number = %d" % table_number)
            oldorderList = self.cursor.fetchone()
            try:
                oldorderList = oldorderList[0]
                neworderList = oldorderList + " %s" % m_name
            except:
                neworderList = ""
            
            self.cursor.execute("UPDATE r_table set tableorderList = '%s' where table_number = %d" % (neworderList, table_number))
            self.db.commit()


            updateSelectedList()
            selectedbox.clear()

        
        #label set up
        lbl_nowList = tk.Label(newWindow, text='此桌已點清單', bg='yellow', font=('微軟正黑體', 20))
        lbl_nowList.place(x=20,y=30,width=291,height=30)
        lbl_bg1 = tk.Label(newWindow, relief = "ridge")
        lbl_bg1.place(x=20,y=60,width=291,height=423)
        lbl_addList = tk.Label(newWindow, text='餐點清單', bg='yellow', font=('微軟正黑體', 20))
        lbl_addList.place(x=330,y=30,width=250,height=30)
        lbl_bg2 = tk.Label(newWindow, relief = "ridge")
        lbl_bg2.place(x=330,y=60,width=251,height=422)

        #button set up
        bt_delete = tk.Button(newWindow, text='刪除餐點', font=('微軟正黑體', 12), command=delete)
        bt_delete.place(x=130,y=430,width=73,height=33)
        bt_add = tk.Button(newWindow, text='添加餐點', font=('微軟正黑體', 12), command=menuSelect)
        bt_add.place(x=420,y=430,width=73,height=32)
        #make a listbox
        tableorderListbox = tk.Listbox(newWindow)
        tableorderListbox.place(x=60,y=90,width=212,height=314)
        menuListbox = tk.Listbox(newWindow)
        menuListbox.place(x=350,y=90,width=212,height=314)

        updateSelectedList()
        getMenu()
        
        
    def addTableMenu(self):
        lbl = tk.Label(self.root, text = '桌子 %d' % (self.tableNumber + 1), font = ('微軟正黑體', 16))
        lbl.place(x = 90, y = 110 + self.tableNumber * 40, width = 70, height = 35)

        sets=("空","正在使用","需清潔")
        var=tk.StringVar(self.root) 
        var.set("空")

        opm=tk.OptionMenu(self.root, var, *sets)
        opm.place(x=180,y=110 + self.tableNumber * 40,width=100,height=35)
        
        bt = tk.Button(self.root, text = '點餐 %d' % (self.tableNumber + 1), font = ('微軟正黑體', 12), command=lambda: self.changeList(bt.cget('text')[3]))
        
        bt.place(x=300,y=110+ self.tableNumber * 40,width=50,height=35)
        
        self.tableNumber += 1
    
    def open(self):
        
        self.root.mainloop()


    def showstaff(self):
        self.cursor.execute("SELECT * FROM members where position = 'staff'")
        results = self.cursor.fetchall()
        print(results)

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







