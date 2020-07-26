from tkinter import *
from pizzapy import *
'''
First_Name = 'Javier'
Last_Name = 'Vasquez'
Email = 'javi.2808@hotmail.com'
Phone = '8323897249'
Address_1 = '2111 Clearfield Springs Ct, Pearland, TX, 77581'
Address_2 = '1701 N Quaker Ave Apt#1014, Lubbock, TX, 79416'

pearlandAddy = Customer(First_Name, Last_Name, Email, Phone, Address_1)
lubbyAddy = Customer(First_Name, Last_Name, Email, Phone, Address_2)

pearlandDominos = StoreLocator.find_closest_store_to_customer(pearlandAddy)
lubbyDominos = StoreLocator.find_closest_store_to_customer(lubbyAddy)
'''

win = Tk()
win.title("Pizza Ordering Machine")
win.geometry("310x350")

Blank_Space_0 = Label(win, text = "     ")
Blank_Space_0.grid(column = 0, row = 0)

Blank_Space_1 = Label(win, text = "     ")
Blank_Space_1.grid(column = 100, row = 0)

Order_1 = Label(win, text = "Peperoni Pizza")
Order_1.grid(column = 1, row = 1)
Order_1_Amount = Entry(win, width = 3)
Order_1_Amount.grid(column = 2, row = 1)

Order_2 = Label(win, text = "Supreme Pizza")
Order_2.grid(column = 1, row = 2)
Order_2_Amount = Entry(win, width = 3)
Order_2_Amount.grid(column = 2, row = 2)

Blank_Space_2 = Label(win, text = "            ")
Blank_Space_2.grid(column = 3, row = 1)

Order_3 = Label(win, text = "Cheese Pizza")
Order_3.grid(column = 4, row = 1)
Order_3_Amount = Entry(win, width = 3)
Order_3_Amount.grid(column = 5, row = 1)

Order_4 = Label(win, text = "Mushroom Pizza")
Order_4.grid(column = 4, row = 2)
Order_4_Amount = Entry(win, width = 3)
Order_4_Amount.grid(column = 5, row = 2)

Search_Label = Label(win, text = "Search for an item:")
Search_Label.place(x = 18, y = 70)
Search_Box = Entry(win, width = 45)
Search_Box.place(x = 20, y = 90)

win.mainloop()