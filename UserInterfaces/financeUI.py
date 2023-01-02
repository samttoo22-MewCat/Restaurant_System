import time
import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk

#window set up
root = tk.Tk() 
root.title('Restaurant System - Finance')
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)


#tree set up
tree=ttk.Treeview(root,columns=("salary list"))
tree.heading("#0",text="員工")
tree.heading("#1",text="薪水")
tree.column("#0",minwidth=0,width=120)
tree.column("#1",minwidth=0,width=120)

staffList = ["a", "b", "c", "d"]
salaryList = [100, 25, 20, 50]


for i in range (len(staffList)):
    tree.insert("",index="end",text=staffList[i],values=salaryList[i])

tree.place(x=340,y=70,width=240,height=330)

#tree set up
treeSell=ttk.Treeview(root,columns=("sell list"))
treeSell.heading("#0",text="名稱")
treeSell.heading("#1",text="成本")
treeSell.heading("#2",text="售價")
treeSell.column("#0",minwidth=0,width=100)
treeSell.column("#1",minwidth=0,width=100)
treeSell.column("#2",minwidth=0,width=100)

sellList = ["fish", "soup", "cake", "salad"]
costList = [100, 25, 20, 50]
sumList = [2000, 500, 800, 50]

for i in range (len(staffList)):
    treeSell.insert("",index="end",text=staffList[i],values=(salaryList[i], sumList[i]))

treeSell.place(x=20,y=70,width=300,height=330)

#label set up
lbl_title1 = tk.Label(root, text="員工薪資表", font=("Arial", 20), bg="#1E90FF")
lbl_title1.place(x=340,y=30,width=240,height=31)
lbl_title2 = tk.Label(root, text="賣出餐點", font=("Arial", 20), bg="#1E90FF")
lbl_title2.place(x=20,y=30,width=300,height=31)
lbl_sumIn = tk.Label(root, font = ("Arial", 15), relief="groove")
lbl_sumIn["text"] = "總收入 :\n" + str(1000)
lbl_sumIn.place(x=20,y=410,width=180,height=77)
lbl_sumOut = tk.Label(root, font = ("Arial", 15), relief="groove")
lbl_sumOut["text"] = "總支出 :\n" + str(700)
lbl_sumOut.place(x=210,y=410,width=180,height=77)
lbl_sumEarn = tk.Label(root, font = ("Arial", 15), relief="groove")
lbl_sumEarn["text"] = "盈餘 :\n" + str(300)
lbl_sumEarn.place(x=400,y=410,width=180,height=77)

root.mainloop()