import tkinter as tk

#window set up
root = tk.Tk() 
root.title('餐廳系統-人員效率介面')
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

#label set up
lbl_Account = tk.Label(root, text="人員ID", fg="black", font=("Arial", 12))
lbl_Account.place(x=40,y=30,width=116,height=35)

#message set up
msg =tk.Message(root,font=("Arial",18,"bold"), relief = "solid",fg='#00CACA')
msg.place(x=50,y=80,width=501,height=370)

def showMessage():
    msg["text"] = "訊息"

#entry set up
entry_ID = tk.Entry(root)
entry_ID.place(x=160,y=30,width=252,height=33)

#button set up
bt_Search = tk.Button(root, text="搜尋", command=showMessage)
bt_Search.place(x=430,y=30,width=70,height=33)

root.mainloop()