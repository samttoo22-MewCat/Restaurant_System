import pymysql
#import staffUI as SUI
import datetime
import time


class cuUI():
    def __init__(self, table_number):
        from datetime import datetime
        self.db = pymysql.connect(host='localhost',
            user='root',
            password='910925As',
            database='test')
        self.cursor = self.db.cursor()
        self.table_number = table_number
        self.startTime = datetime.now()
        self.endTime = datetime.now()

    def getBill(self):
        from datetime import datetime       
        self.cursor.execute("SELECT * FROM orders")
        results = self.cursor.fetchall()
        first = []
        second = []
        third = []
        for result in results:
            time = result[0]
            m_name = result[1]
            table_number = result[2]
            
            order_time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
            
            self.cursor.execute("SELECT * FROM menu where m_name = '%s'" % str(m_name))
            results = self.cursor.fetchall()
            m_type = results[0][0]
            m_price = results[0][2]
            if(order_time >= self.startTime and order_time < self.endTime and table_number == self.table_number):
                #在這桌的用餐時間內的訂單才算錢
                if(m_type == '開胃菜' or m_type == '沙拉'):
                    first.append("- %s: %d元" % (m_name, m_price))
                elif(m_type == '飲品'):
                    second.append("- %s: %d元" % (m_name, m_price))
                else:
                    third.append("- %s: %d元" % (m_name, m_price))

        print("帳單如下:")
        for row in first: 
            print(row)
        for row in second: 
            print(row)
        for row in third: 
            print(row)
        print()

    def start(self):
        from datetime import datetime
        self.startTime = datetime.now()
        self.startTime = datetime.strftime(self.startTime, '%Y-%m-%d %H:%M:%S')
        self.startTime = datetime.strptime(self.startTime, '%Y-%m-%d %H:%M:%S')
        self.changeTableTaken(self.table_number, True)

    def end(self):
        from datetime import datetime
        self.endTime = datetime.now()
        self.endTime = datetime.strftime(self.endTime, '%Y-%m-%d %H:%M:%S')
        self.endTime = datetime.strptime(self.endTime, '%Y-%m-%d %H:%M:%S')
        self.changeTableState(self.table_number, "unclean")
        self.changeTableTaken(self.table_number, False)

    def changeTableState(self, table_number, state):
            self.cursor.execute("UPDATE r_table set state = '%s' where table_number = %d" % (str(state), int(table_number)))
            self.db.commit()
    


cuUI = cuUI(1)
cuUI.start()

cuUI.end()