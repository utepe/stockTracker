import csv
import yfinance as yf
from yahoo_fin import stock_info as si 

class stockTracker():
    def __init__(self):
        self.file = csv.reader(open("activity.csv"))
        self.lines = list(self.file)
        self.quantityCol = self.lines[0].index("Quantity")
        self.symbolCol = self.lines[0].index("Symbol")
        self.oldPriceCol = self.lines[0].index("Price")
        self.nowPriceCol = self.lines[0].index("Now")
        self.gainCol = self.lines[0].index("Gain")
        # print(len(self.lines))
    
    def updateNow(self):
        for i in range(1, len(self.lines)):
            self.lines[i][self.nowPriceCol] = si.get_live_price(self.lines[i][self.symbolCol])
            if self.lines[i][self.quantityCol] == "" or self.lines[i][self.oldPriceCol] == "":
                continue
            else:
                self.lines[i][self.gainCol] = str(int(self.lines[i][self.quantityCol])*(float(self.lines[i][self.nowPriceCol]) - float(self.lines[i][self.oldPriceCol])))
        for i in self.lines:
            print(i)    

"""
If Activty == "Sell", calcluated the gain based on the day that the stick was sold
if Acitity == "Buy", calcute the current gain based on in the current stock price
"""

tracker = stockTracker()
tracker.updateNow()