import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self):
        self.root = tk.Tk()
        
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

        self.GButton_579=tk.Button(self.root, activebackground= "#ff8c00", font= ("微軟正黑體", 10), justify= "center", text= "呼叫服務生")
        self.GButton_579.place(x=70,y=130,width=100,height=50)
        self.GButton_577=tk.Button(self.root, activebackground= "#ff8c00", font= ("微軟正黑體", 10), justify= "center", text= "結帳")
        self.GButton_577.place(x=70,y=190,width=100,height=50)


        self.GMessage_741=tk.Message(self.root, fg= "#333333", font= ("微軟正黑體", 10), justify= "center", text= "顯示帳單")
        self.GMessage_741.place(x=200,y=10,width=400,height=400)
    def test(self):
        print("test")
if __name__ == "__main__":
    app = App()
    while(1):
        app.root.after(100, app.test)
    app.root.mainloop()