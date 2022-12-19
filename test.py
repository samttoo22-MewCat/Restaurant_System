import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self):
        self.root = tk.Tk()
        #setting title
        self.root.title("餐廳系統-經理介面")
        #setting window size
        self.width=649
        self.height=504
        self.screenwidth = self.root.winfo_screenwidth()
        self.screenheight = self.root.winfo_screenheight()
        self.alignstr = '%dx%d+%d+%d' % (self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)
        self.root.geometry(self.alignstr)
        self.root.resizable(width=False, height=False)

        self.GButton_926=tk.Button(self.root, bg="#009688", font=('微軟正黑體', 10), justify="center", text="增加桌子數量")
        self.GButton_926.place(x=10,y=10,width=144,height=32)
        self.GButton_926["command"] = self.GButton_926_command

        self.GButton_840=tk.Button(self.root, bg="#1e9fff", font=('微軟正黑體', 10), fg="#000000", justify="center", text="增加工作人員")
        self.GButton_840.place(x=10,y=50,width=144,height=30)
        self.GButton_840["command"] = self.GButton_840_command

        self.GButton_802=tk.Button(self.root, bg="#5fb878", font=('微軟正黑體', 10), fg="#000000", justify="center", text="減少桌子數量")
        self.GButton_802.place(x=170,y=10,width=141,height=32)
        self.GButton_802["command"] = self.GButton_802_command

        self.GLabel_153=tk.Label(self.root, bg="#ffb800", font=('微軟正黑體', 10), fg="#333333", justify="center", text="帳號")
        self.GLabel_153.place(x=10,y=90,width=71,height=30)

        self.GLineEdit_248=tk.Entry(self.root, borderwidth="1px", font=('微軟正黑體', 10), fg="#333333", justify="center")
        self.GLineEdit_248.place(x=80,y=90,width=181,height=30)

        self.GLabel_831=tk.Label(self.root, bg="#ffb800", font=('微軟正黑體', 10), fg="#333333", justify="center", text="密碼")
        self.GLabel_831.place(x=10,y=130,width=70,height=30)

        self.GLabel_717=tk.Label(self.root, bg="#ffb800", font=('微軟正黑體', 10), fg="#333333", justify="center", text="職位")
        self.GLabel_717.place(x=10,y=170,width=70,height=30)

        self.GLineEdit_257=tk.Entry(self.root, borderwidth="1px", font=('微軟正黑體', 10), fg="#333333", justify="center")
        self.GLineEdit_257.place(x=80,y=130,width=181,height=30)

        self.GLineEdit_949=tk.Entry(self.root, borderwidth="1px", font=('微軟正黑體', 10), fg="#333333", justify="center")
        self.GLineEdit_949.place(x=80,y=170,width=181,height=30)

        self.GButton_972=tk.Button(self.root, bg="#1e9fff", font=('微軟正黑體', 10), fg="#000000", justify="center", text="刪除工作人員")
        self.GButton_972.place(x=10,y=210,width=144,height=30)
        self.GButton_972["command"] = self.GButton_972_command

        self.GLabel_653=tk.Label(self.root, bg="#ffb800", font=('微軟正黑體', 10), fg="#333333", justify="center", text="帳號")
        self.GLabel_653.place(x=10,y=250,width=70,height=30)

        self.GLineEdit_295=tk.Entry(self.root, borderwidth="1px", font=('微軟正黑體', 10), fg="#333333", justify="center")
        self.GLineEdit_295.place(x=80,y=250,width=182,height=30)

        self.GButton_774=tk.Button(self.root, bg="#00babd", font=('微軟正黑體', 10), fg="#000000", justify="center", text="查看工資列表")
        self.GButton_774.place(x=360,y=90,width=144,height=30)
        self.GButton_774["command"] = self.GButton_774_command

        self.GButton_936=tk.Button(self.root, bg="#00babd", font=('微軟正黑體', 10), fg="#000000", justify="center", text="查看盈餘狀況")
        self.GButton_936.place(x=360,y=130,width=143,height=30)
        self.GButton_936["command"] = self.GButton_936_command

        self.GButton_29=tk.Button(self.root, bg="#00babd", font=('微軟正黑體', 10), fg="#000000", justify="center", text="查看員工效率")
        self.GButton_29.place(x=360,y=170,width=144,height=30)
        self.GButton_29["command"] = self.GButton_29_command

        self.GButton_91=tk.Button(self.root, bg="#c71585", font=('微軟正黑體', 10), fg="#000000", justify="center", text="刷下")
        self.GButton_91.place(x=10,y=350,width=144,height=30)
        self.GButton_91["command"] = self.GButton_91_command

        self.GButton_335=tk.Button(self.root, bg="#c71585", font=('微軟正黑體', 10), fg="#000000", justify="center", text="刷上")
        self.GButton_335.place(x=10,y=310,width=145,height=30)
        self.GButton_335["command"] = self.GButton_335_command

        self.GMessage_750=tk.Message(self.root, font=('微軟正黑體', 10), fg="#000000", justify="center", text="打卡訊息")
        self.GMessage_750.place(x=170,y=310,width=263,height=162)

    def GButton_926_command(self):
        print("command")


    def GButton_840_command(self):
        print("command")


    def GButton_802_command(self):
        print("command")


    def GButton_972_command(self):
        print("command")


    def GButton_774_command(self):
        print("command")


    def GButton_936_command(self):
        print("command")


    def GButton_29_command(self):
        print("command")


    def GButton_91_command(self):
        print("command")


    def GButton_335_command(self):
        print("command")
    def open(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.open()
