import pymysql
import tkinter as tk
from tkinter import messagebox
import staffUI
import cookUI


class verifyUI():
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
            user='root',
            password='910925As',
            database='test')
        self.cursor = self.db.cursor()
        self.postion = ""
        self.opened = False
        self.root = tk.Tk()
        #setting title
        self.root.title("餐廳系統-登入介面")
        #setting window size
        self.width=400
        self.height=175
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        self.alignstr = '%dx%d+%d+%d' % (self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)
        self.root.geometry(self.alignstr)
        self.root.resizable(width=False, height=False)

        self.GLabel_748=tk.Label(self.root, bg="#ffb800", font=('微軟正黑體', 10), fg = "#333333", justify= "center", text= "帳號")
        self.GLabel_748.place(x=10,y=30,width=105,height=31)

        self.GLabel_631=tk.Label(self.root, bg="#ffb800", font=('微軟正黑體', 10), fg = "#333333", justify= "center", text= "密碼")
        self.GLabel_631.place(x=10,y=70,width=105,height=30)

        self.GButton_980=tk.Button(self.root, bg="#00ced1", font=('微軟正黑體', 10), fg = "#000000", justify= "center", text= "登入")
        self.GButton_980.place(x=10,y=120,width=107,height=30)
        self.GButton_980["command"] = self.vbt

        self.GLineEdit_860=tk.Entry(self.root, borderwidth= "1px", font = ('微軟正黑體', 10), fg = "#000000", justify = "left")
        self.GLineEdit_860.place(x=120,y=30,width=205,height=32)

        self.GLineEdit_264=tk.Entry(self.root, borderwidth= "1px", font = ('微軟正黑體', 10), fg = "#000000", justify = "left")
        self.GLineEdit_264.place(x=120,y=70,width=206,height=30)
    def verify(self, username, password):
        self.cursor.execute("SELECT * FROM members")
        results = self.cursor.fetchall()

        for row in results:
            db_username = row[0]
            db_password = row[2]

            if str(username) == db_username and str(password) == db_password:
                self.postion = row[1]
                return True
            else:
                pass
        return False
    def vbt(self):
        username = self.GLineEdit_860.get()
        password = self.GLineEdit_264.get()
        if(self.verify(username, password)):
            self.cursor.execute("SELECT position FROM members where user_id = '%s'" % username)
            position = self.cursor.fetchone()
            position = position[0]
            if(position == "manager"):
                pass
            elif(position == "staff"):
                if(self.opened == False):
                    self.opened = True
                    UI = staffUI.staffUI("%s" % username)
                    UI.open()
                    self.opened = False
                else:
                    messagebox.showwarning(title="登入失敗", message="你已經有登入一次了。")
                
            elif(position == "Ptworker"):
                pass
            elif(position == "reception"):
                pass
            elif(position == "cook"):
                if(self.opened == False):
                    self.opened = True
                    UI = cookUI.cookUI("%s" % username)
                    UI.open()
                    self.opened = False
                else:
                    messagebox.showwarning(title="登入失敗", message="你已經有登入一次了。")

        else:
            messagebox.showwarning(title="登入失敗", message="帳號或密碼錯誤。")
    def open(self):
        self.root.mainloop()
    

vUI = verifyUI()
vUI.open()
    