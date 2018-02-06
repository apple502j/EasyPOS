import tkinter as ti
from math import ceil
import tkinter.messagebox as tm
from pprint import pprint
import datetime

'''
    (C) 2018 apple502j All rights reserved.
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

# settings

root=ti.Tk()
root.title("TK POS")
root.geometry("480x360")

TAX=0
#Tax: If it doesn't exist, put 0

POS_FIRST="Example Shop"
POS_ADD="{y} yen, bought."
POS_DISCOUNT="{p} percent, discount. {y} yen."
POS_TAX="{p} percent tax."
POS_DONE="Done:{y} yen, {i} items."

RFILE="receipt.txt"

# end settings

# begin TKInter

global bought
bought=[]

global receipt
receipt=[POS_FIRST]

def buyOne(ev):
    try:
        yen=money.get()
        if yen == "":
            return
        yenInteger=int(yen)
        bought.append(yenInteger)
        receipt.append(POS_ADD.format(y=str(yenInteger)))
    except ValueError:
        # Don't worry about it.
        pass
    finally:
        money.delete(0, ti.END)

def discountLast(ev):
    try:
        if len(bought) == 0:
            return
        dp=discount.get()
        if dp == "":
            return
        if dp[0] == "-":
            return
        dpInteger=100 - int(dp)
        lastNum=len(bought)-1
        bought[lastNum] = ceil(bought[lastNum] * (dpInteger / 100))
        receipt.append(POS_DISCOUNT.format(p=str(dpInteger),y=bought[lastNum]))
    except ValueError:
        pass
def showResult(ev):
    global bought
    try:
        count=len(bought)
        if count==0:
            allThings=0
        else:
            allThings=sum(bought)
            allThings=allThings * (1+TAX)
            receipt.append(POS_TAX.format(p=str(TAX)))
        tm.showinfo('Done',"{m} yen, {i} items.".format(m=allThings,i=count))
        receipt.append(POS_DONE.format(y=str(allThings),i=str(count)))
        dt=datetime.datetime.now().strftime('%Y/%m/%d (%A) %H:%M')
        receipt.append(dt)
        pprint(receipt)
        with open(RFILE,"w") as receiptFile:
            receiptFile.write('\n'.join(receipt))
    except:
        pass
    finally:
        bought=[]

money = ti.Entry(width=10)
money.place(x=10,y=10)

discount = ti.Entry(width=10)
discount.place(x=10,y=50)
discount.insert(ti.END,"0")

addbtn = ti.Button(text="Add",width=10)
addbtn.bind("<Button-1>",buyOne)
addbtn.place(x=100,y=10)

disbtn = ti.Button(text="% Discount",width=25)
disbtn.bind("<Button-1>",discountLast)
disbtn.place(x=100,y=50)

showbtn = ti.Button(text="OK",width=10)
showbtn.bind("<Button-1>",showResult)
showbtn.place(x=10,y=100)

# end TKInter
if __name__=="__main__":
    root.mainloop()
