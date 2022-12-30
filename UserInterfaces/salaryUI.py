import tkinter as tk

class salaryUI():
    def __init__(self):

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
        self.sets=("Tom","John","Mary", "Karen", "Jack")

        #change staff
        self.var1=tk.StringVar(self.root) 
        self.var1.set("Staff List")

        #show staff
        self.opm_1=tk.OptionMenu(self.root, self.var1, *self.sets)
        self.opm_1.place(x=130,y=50,width=354,height=30)

        #Label set up
        self.lbl_time = tk.Label(self.root,font=("微軟正黑體", 20))
        self.lbl_salary=tk.Label(self.root, font=("微軟正黑體", 80))

        #salary table
        self.salary=[10000, 50, 60]
        #Button set up
        self.bt_lastWeek = tk.Button(self.root, text="Last Week", bg="#1E90FF",command=showLastWeek)
        self.bt_lastWeek.place(x=140,y=120,width=78,height=61)
        self.bt_lastHalfMonth = tk.Button(self.root, text="Last Half \nof Month", bg="#1E90FF", command=showLastHalfMonth)
        self.bt_lastHalfMonth.place(x=270,y=120,width=78,height=60)
        self.bt_lastMonth = tk.Button(self.root, text="Last Month", bg="#1E90FF", command=showLastMonth)
        self.bt_lastMonth.place(x=400,y=120,width=78,height=61)

    def showLastWeek():
        lbl_time["text"] = "Last Week Salary :"
        lbl_time.place(x=100,y=220,width=400,height=66)
        lbl_salary["text"] = salary[0]
        lbl_salary.place(x=160,y=320,width=294,height=80)
    def showLastHalfMonth():
        lbl_time["text"] = "Last Half of Month Salary :"
        lbl_time.place(x=100,y=220,width=400,height=66)
        lbl_salary["text"] = salary[1]
        lbl_salary.place(x=160,y=320,width=294,height=80)
    def showLastMonth():
        lbl_time["text"] = "Last Month Salary :"
        lbl_time.place(x=100,y=220,width=400,height=66)
        lbl_salary["text"] = salary[2]
        lbl_salary.place(x=160,y=320,width=294,height=80)



root.mainloop()