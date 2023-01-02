import tkinter as tk
import pymysql

class salaryUI():
    def __init__(self):
        def getStaffList():
            self.cursor.execute("SELECT user_id FROM members")
            results = self.cursor.fetchall()
            for result in results:
                user_id = result[0]
                self.staffList.append(user_id)

        self.db = pymysql.connect(host='localhost',
            user='root',
            password='910925As',
            database='test',
            autocommit=True)
        self.cursor = self.db.cursor()
        #window set up
        self.root = tk.Tk() 
        self.root.title('餐廳系統-員工薪資介面')
        width=600
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        #staff list
        self.staffList=[]
        getStaffList()

        #change staff
        self.var1=tk.StringVar(self.root) 
        self.var1.set("Staff List")

        #show staff
        self.opm_1=tk.OptionMenu(self.root, self.var1, *self.staffList)
        self.opm_1.place(x=130,y=50,width=354,height=30)

        #Label set up
        self.lbl_time = tk.Label(self.root,font=("微軟正黑體", 20))
        self.lbl_salary=tk.Label(self.root, font=("微軟正黑體", 80))

        #salary table
        self.salary=[10000, 50, 60]
        #Button set up
        self.bt_lastWeek = tk.Button(self.root, text="Last Week", bg="#1E90FF",command=self.showLastWeek)
        self.bt_lastWeek.place(x=140,y=120,width=78,height=61)
        self.bt_lastHalfMonth = tk.Button(self.root, text="Last Half \nof Month", bg="#1E90FF", command=self.showLastHalfMonth)
        self.bt_lastHalfMonth.place(x=270,y=120,width=78,height=60)
        self.bt_lastMonth = tk.Button(self.root, text="Last Month", bg="#1E90FF", command=self.showLastMonth)
        self.bt_lastMonth.place(x=400,y=120,width=78,height=61)

    def showLastWeek(self):
        self.lbl_time["text"] = "上星期薪資列表 :"
        self.lbl_time.place(x=100,y=220,width=400,height=66)
        self.lbl_salary["text"] = self.salary[0]
        self.lbl_salary.place(x=160,y=320,width=294,height=80)
    def showLastHalfMonth(self):
        self.lbl_time["text"] = "上個半月薪資列表 :"
        self.lbl_time.place(x=100,y=220,width=400,height=66)
        self.lbl_salary["text"] = self.salary[1]
        self.lbl_salary.place(x=160,y=320,width=294,height=80)
    def showLastMonth(self):
        self.lbl_time["text"] = "Last Month Salary :"
        self.lbl_time.place(x=100,y=220,width=400,height=66)
        self.lbl_salary["text"] = self.salary[2]
        self.lbl_salary.place(x=160,y=320,width=294,height=80)

    def open(self):
        self.root.mainloop()

UI = salaryUI()
UI.open()