import tkinter as tk
import tkinter.messagebox

#window set up
root = tk.Tk() 
root.title('Restaurant System')
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

#label set up
lbl_1 = tk.Label(root, relief = "ridge")
lbl_1.place(x=20,y=40,width=426,height=447)
lbl_2 = tk.Label(root, relief = "ridge")
lbl_2.place(x=460,y=40,width=120,height=447)
lbl_3 = tk.Label(root, bg = "yellow", text='Uncleaned Table', fg='black', font=('Arial', 20), anchor='center')
lbl_3.place(x=20,y=10,width=426,height=30)
lbl_4 = tk.Label(root, bg = "yellow", text='Pounch', fg='black', font=('Arial', 20), anchor='center')
lbl_4.place(x=460,y=10,width=120,height=30)

#show succeed message
def succeed():
    lbl_1 = tk.Label(root, text="pounch \n successfully")
    lbl_1.place(x=480,y=100,width=80,height=120)

#delete selected table
def finish():
    selectedPlace = mylistbox.curselection()
    mylistbox.delete(selectedPlace)

#make a listbox
mylistbox = tk.Listbox(root)
for i in ['Table 1','Table 2','Table 3','Table 4','Table 5']:
    mylistbox.insert(tk.END, i)
mylistbox.place(x=80,y=100,width=300,height=150)

#button set up
bt_1 = tk.Button(root, text='finish', font=('Arial', 15), command=finish)
bt_1.place(x=190,y=300,width=70,height=25)
bt_2 = tk.Button(root, text='pounch in', font=('Arial', 12), command=succeed)
bt_2.place(x=478,y=400,width=88,height=30)
bt_3 = tk.Button(root, text='pounch out', font=('Arial', 12), command=succeed)
bt_3.place(x=478,y=440,width=88,height=30)

root.mainloop()