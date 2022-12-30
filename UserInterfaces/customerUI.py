import pymysql
#import staffUI as SUI
import datetime
import time
import tkinter as tk


class cuUI():
    def __init__(self, table_number, root):
        from datetime import datetime
        self.db = pymysql.connect(host='localhost',
            user='root',
            password='910925As',
            database='test',
            autocommit=True)
        self.cursor = self.db.cursor()
        self.table_number = table_number
        self.startTime = datetime.now()
        self.endTime = datetime.now()
        self.root = tk.Toplevel(root)
        #setting title
        self.root.title("餐廳系統-顧客介面")
        #setting window size
        self.width=600
        self.height=500
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        self.alignstr = '%dx%d+%d+%d' % (self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)
        self.root.geometry(self.alignstr)
        self.root.resizable(width=False, height=False)


        self.lbl=tk.Label(self.root, font= ("微軟正黑體", 12), justify= "center", text= "桌號: %d" % int(self.table_number))
        self.lbl.place(x=70,y=70,width=100,height=50)
        self.GButton_579=tk.Button(self.root, activebackground= "#ff8c00", font= ("微軟正黑體", 10), justify= "center", text= "呼叫服務生")
        self.GButton_579.place(x=70,y=130,width=100,height=50)
        


        self.billListbox=tk.Listbox(self.root, fg= "#333333", font= ("微軟正黑體", 10), justify= "left")
        self.billListbox.place(x=200,y=10,width=350,height=400)
        self.root.after(100, self.getBill)
        self.root.protocol("WM_DELETE_WINDOW", lambda x = None: self.root.destroy())
    
    def getBill(self):
        from datetime import datetime       
        self.cursor.execute("select tableorderList from r_table where table_number = %d" % int(self.table_number))
        results = self.cursor.fetchall()
        first = []
        second = []
        third = []
        sum = 0
        orderList = results[0][0]
        orderList = orderList.split(" ")

            
        for order in orderList:
            self.cursor.execute("SELECT * FROM menu where m_name = '%s'" % str(order))
            results = self.cursor.fetchone()
            m_type = results[0]
            m_name = results[1]
            m_price = results[2]
            try:
                sum += int(m_price)
            except:
                print(m_price)
            self.billListbox.delete(0, tk.END)
            
            if(m_type == '開胃菜' or m_type == '沙拉'):
                first.append("- %s: %d元" % (m_name, m_price))
            elif(m_type == '飲品'):
                second.append("- %s: %d元" % (m_name, m_price))
            else:
                third.append("- %s: %d元" % (m_name, m_price))

        for row in first: 
            self.billListbox.insert(tk.END, row)
        for row in second: 
            self.billListbox.insert(tk.END, row)
        for row in third: 
            self.billListbox.insert(tk.END, row)
        self.billListbox.insert(tk.END, ("總共 " + str(sum) + " 元"))
        self.root.after(100, self.getBill)
        
    def payBill(self):
        self.cursor.execute("update r_table set tableorderList = '' where table_number = '%s'" % self.table_number)
        self.db.commit()
    


    def start(self):
        from datetime import datetime
        self.startTime = datetime.now()
        self.startTime = datetime.strftime(self.startTime, '%Y-%m-%d %H:%M:%S')
        self.startTime = datetime.strptime(self.startTime, '%Y-%m-%d %H:%M:%S')


    def end(self):
        from datetime import datetime
        self.endTime = datetime.now()
        self.endTime = datetime.strftime(self.endTime, '%Y-%m-%d %H:%M:%S')
        self.endTime = datetime.strptime(self.endTime, '%Y-%m-%d %H:%M:%S')


    def changeTableState(self, table_number, state):
        self.cursor.execute("UPDATE r_table set state = '%s' where table_number = %d" % (str(state), int(table_number)))
        self.db.commit()
    
    def open(self):
        
        self.start()
        
        self.root.destroy()
        self.root.mainloop()

