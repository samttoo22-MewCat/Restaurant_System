import pymysql
import datetime
import staffUI
import customerUI
import PTworkerUI
import receptionUI

import time
import os
import tkinter as tk

class cookUI():
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
        def finishOrder():
            selectedPlace = self.prepareListbox.curselection()
            selected = self.prepareListbox.get(selectedPlace)
            selected = selected.split(" - ")
            m_name = selected[0]
            time = selected[1]
            self.cursor.execute("delete from orders where m_name = '%s' and time = '%s'" % (m_name, time))
            self.db.commit()

            self.prepareListbox.delete(selectedPlace)
            
        
        self.db = pymysql.connect(host='localhost',
            user='root',
            password='910925As',
            database='test',
            autocommit=True)
        self.cursor = self.db.cursor()
        self.user_id = str(user_id)
        self.prepareList = []
        self.root = tk.Toplevel(root)
        self.root.title('餐廳系統-廚師介面')

        self.width=750
        self.height=500
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        self.alignstr = '%dx%d+%d+%d' % (self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)

        self.root.geometry(self.alignstr)
        self.root.resizable(width=False, height=False)
        
        #label and button set up
        self.lbl_1 = tk.Label(self.root, relief = "ridge")
        self.lbl_1.place(x=20,y=40,width=426,height=447)
        self.lbl_2 = tk.Label(self.root, relief = "ridge")
        self.lbl_2.place(x=460,y=40,width=270,height=447)
        self.lbl_3 = tk.Label(self.root, bg = "yellow", text='餐點準備清單', fg='black', font=('微軟正黑體', 15), anchor='center')
        self.lbl_3.place(x=20,y=10,width=426,height=30)
        self.lbl_4 = tk.Label(self.root, bg = "yellow", text='打卡', fg='black', font=('微軟正黑體', 15), anchor='center')
        self.lbl_4.place(x=460,y=10,width=270,height=30)
       
        self.prepareListbox = tk.Listbox(self.root, font=('微軟正黑體', 10))
        self.prepareListbox.place(x=40,y=90,width=390,height=330)
        
        
        self.bt_2 = tk.Button(self.root, text='刷上', font=('微軟正黑體', 12), command=clockIn)
        self.bt_2.place(x=478,y=440,width=88,height=30)
        self.bt_3 = tk.Button(self.root, text='刷下', font=('微軟正黑體', 12), command=clockOut)
        self.bt_3.place(x=624,y=440,width=88,height=30)
        #button set up
        self.bt_1 = tk.Button(self.root, text='完成', font=('微軟正黑體', 12), command=finishOrder)
        self.bt_1.place(x=190,y=440,width=88,height=30)
        self.root.protocol("WM_DELETE_WINDOW", lambda x = None: os._exit(0))
        

    def updatePrepareList(self):
        
        first = []
        second = []
        third = []
        newOrder = []
        currentOrder = self.prepareListbox.get(0, tk.END)
        self.cursor.execute("SELECT * FROM orders")
        results = self.cursor.fetchall()
        for result in results:
            time = result[0]
            m_name = result[1]
            t_number = result[2]
            self.cursor.execute("SELECT m_type FROM menu where m_name = '%s'" % m_name)
            
            m_type = self.cursor.fetchone()
            m_type = m_type[0]
            newOrder.append("%s - %s - 第 %d 桌" % (m_name, time, t_number))

        for i in newOrder:
            #第一次把這個餐點放入訂單
            if(i not in currentOrder):
                if(m_type == '開胃菜' or m_type == '沙拉'):
                    first.append(i)
                    
                elif(m_type == '飲品'):
                    second.append(i) 
                else:
                    #主菜類
                    third.append(i)
            #已經被放入訂單過/同名訂單還未放入
            else:
                
                currentCount = currentOrder.count(i)
                newCount = newOrder.count(i)
                if(currentCount == 1):
                    if(m_type == '開胃菜' or m_type == '沙拉'):
                        for j in range(newCount - 1):
                            first.append(i)
                    
                    elif(m_type == '飲品'):
                        for j in range(newCount - 1):
                            second.append(i) 
                    else:
                        #主菜類
                        for j in range(newCount - 1):
                            third.append(i)
     
        for i in first:
            self.prepareListbox.insert(tk.END, i)  
        for i in second:
            self.prepareListbox.insert(tk.END, i)
        for i in third:
            self.prepareListbox.insert(tk.END, i)
        self.root.after(100, self.updatePrepareList)

    
    def open(self):
        self.root.after(100, self.updatePrepareList)
        self.root.mainloop()
        
root = tk.Tk()
root.withdraw()
UI = cookUI("samttoo22", root)
UI.updatePrepareList()

UI2 = staffUI.staffUI("000", root)
UI3 = customerUI.cuUI(1, root)
UI4 = PTworkerUI.PtUI("001", root)
UI5 = receptionUI.reUI("002", root)
UI.open()










