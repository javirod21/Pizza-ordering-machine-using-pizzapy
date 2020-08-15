from tkinter import *
from pizzapy import *
from tkinter import messagebox

First_Name = 'Javier'
Last_Name = 'Vasquez'
Email = 'javi.2808@hotmail.com'
Phone = '8323897249'
Address_1 = '2111 Clearfield Springs Ct, Pearland, TX, 77581'
Address_2 = '1701 N Quaker Ave Apt 1014, Lubbock, TX, 79416'

customer = ""
dominos = ""
order = ""
order_num = 0
card = CreditCard('4400665801416734', '0323', '615', '77581')

# Saved info for lubbock and pearland addressees
Pearland_Addy = Customer(First_Name, Last_Name, Email, Phone, Address_1)
Lubby_Addy = Customer(First_Name, Last_Name, Email, Phone, Address_2)

# Find nearest open store to both addresses
Pearland_Dominos = StoreLocator.find_closest_store_to_customer(Pearland_Addy)
Lubby_Dominos = StoreLocator.find_closest_store_to_customer(Lubby_Addy)

# Get the menu of those stores
Pearland_Menu = Pearland_Dominos.get_menu()
Lubby_Menu = Lubby_Dominos.get_menu()


def Page_Open(page):
    page.tkraise()


# Gets data from the search entry box and creates a new window that
# displays the code, name, and price for all items with the keyword
# in their name
def Search_Item():
    item = Search_Box.get()
    Searched_Item = Pearland_Menu.search(Name=item)
    print(Searched_Item[0])
    Search_Popup = Tk()
    Search_Popup.wm_title(item + " items")

    scrollbar = Scrollbar(Search_Popup)
    Items_List = Listbox(Search_Popup, width=75, height=25, yscrollcommand=scrollbar.set)
    scrollbar.config(command=Items_List.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    Items_List.pack()

    for i in range(0, len(Searched_Item)):
        Items_List.insert(END, Searched_Item[i])

    Btn = Button(Search_Popup, text='Okay', command=Search_Popup.destroy)
    Btn.pack()

    Search_Popup.mainloop()


# Starts a new order based on the selected store. Clears any previous orders that may have existed
def Select_Store(cus, dom):
    global customer, dominos, order, Order_Scrollbar_X, Order_Scrollbar_Y, Order_List, Order_Canvas, order_num
    customer = cus
    dominos = dom
    order_num = 0

    # Highlight selected button
    if customer == Pearland_Addy:
        Pearland_Btn.config(bg="#EBA55D")
        Lubby_Btn.config(bg="#E1E1E1")
    else:
        Pearland_Btn.config(bg="#E1E1E1")
        Lubby_Btn.config(bg="#EBA55D")

    # Reset the contents of the GUI list
    Order_Canvas = Canvas(Menu_Win, width=285, height=285, bg="#E1E1E1")
    Order_Canvas.place(x=18, y=215)

    Order_Scrollbar_Y = Scrollbar(Order_Canvas)
    Order_Scrollbar_X = Scrollbar(Order_Canvas, orient='horizontal')
    Order_List = Listbox(Order_Canvas, width=45, height=18, xscrollcommand=Order_Scrollbar_X.set,
                         yscrollcommand=Order_Scrollbar_Y.set)
    Order_Scrollbar_Y.config(command=Order_List.yview)
    Order_Scrollbar_Y.pack(side=RIGHT, fill=Y)
    Order_Scrollbar_X.config(command=Order_List.xview)
    Order_Scrollbar_X.pack(side=BOTTOM, fill=X)
    Order_List.pack()

    order = Order.begin_customer_order(customer, dominos)


# Adds item to order
def Add_To_Order(item, done):
    global customer, dominos, order, order_num
    # First check if a location has been selected
    if customer == "" or dominos == "":
        messagebox.showerror("Error", "Select a location first.")
        return

    # Adds item to order and displays it on the list
    order.add_item(item)
    Order_List.insert(END, order.data['Products'][order_num])
    order_num += 1

    if done:
        Place_Order()


# Places order to local dominos
def Place_Order():
    global card
    order.place(card)
    dominos.place_order(order, card)
    messagebox.showerror("Order Placed!", "Your order has been placed and will be delivered to %s" % customer.address)


# BEGINNING OF GUI CODE
Menu_Win = Tk()
Menu_Win.title("Pizza Ordering Machine")
Menu_Win.geometry("325x575")

Blank_Space_0 = Label(Menu_Win, text="     ")
Blank_Space_0.grid(column=0, row=0)

Blank_Space_1 = Label(Menu_Win, text="     ")
Blank_Space_1.grid(column=100, row=0)

# 4 presets
Order_1 = Label(Menu_Win, text="Pepperoni Pizza")
Order_1.grid(column=1, row=1)
Order_1_Btn = Button(Menu_Win, text="Add", command=lambda: Add_To_Order("14TPFEAST", True))
Order_1_Btn.grid(column=2, row=1)

Order_2 = Label(Menu_Win, text="Deluxe Pizza")
Order_2.grid(column=1, row=2)
Order_2_Btn = Button(Menu_Win, text="Add", command=lambda: Add_To_Order("14SCDELUX", True))
Order_2_Btn.grid(column=2, row=2)

Blank_Space_2 = Label(Menu_Win, text="        ")
Blank_Space_2.grid(column=3, row=1)

Order_3 = Label(Menu_Win, text="Cheese Pizza")
Order_3.grid(column=4, row=1)
Order_3_Btn = Button(Menu_Win, text="Add", command=lambda: Add_To_Order("P14IBKCZ", True))
Order_3_Btn.grid(column=5, row=1)

Order_4 = Label(Menu_Win, text="Meat Lovers Pizza")
Order_4.grid(column=4, row=2)
Order_4_Btn = Button(Menu_Win, text="Add", command=lambda: Add_To_Order("14SCMEATZA", True))
Order_4_Btn.grid(column=5, row=2)

# Search the code of an item by name
Search_Label = Label(Menu_Win, text="Search for an item:")
Search_Label.place(x=18, y=80)
Search_Box = Entry(Menu_Win, width=30)
Search_Box.place(x=20, y=100)
Search_Btn = Button(Menu_Win, text="Search for Item", width=12, command=Search_Item)
Search_Btn.place(x=210, y=96)

# Enter the code of an item to add it to the order
Entry_Label = Label(Menu_Win, text="Enter an item code:")
Entry_Label.place(x=18, y=120)
Entry_Box = Entry(Menu_Win, width=30)
Entry_Box.place(x=20, y=140)
Entry_Btn = Button(Menu_Win, text="Enter Code", width=12, command=lambda: Add_To_Order(Entry_Box.get(), False))
Entry_Btn.place(x=210, y=135)

# Buttons that place order to pearland or lubby
Pearland_Btn = Button(Menu_Win, text="New Order to Pearland", bg="#E1E1E1", width=18,
                      command=lambda: Select_Store(Pearland_Addy, Pearland_Dominos))
Pearland_Btn.place(x=18, y=170)

Lubby_Btn = Button(Menu_Win, text="New Order to Lubbock", bg="#E1E1E1", width=18,
                   command=lambda: Select_Store(Lubby_Addy, Lubby_Dominos))
Lubby_Btn.place(x=168, y=170)

# List that displays all items added to the order
Order_Canvas = Canvas(Menu_Win, width=285, height=285, bg="#E1E1E1")
Order_Canvas.place(x=18, y=215)

Order_Scrollbar_Y = Scrollbar(Order_Canvas)
Order_Scrollbar_X = Scrollbar(Order_Canvas, orient='horizontal')
Order_List = Listbox(Order_Canvas, width=45, height=18, xscrollcommand=Order_Scrollbar_X.set,
                     yscrollcommand=Order_Scrollbar_Y.set)
Order_Scrollbar_Y.config(command=Order_List.yview)
Order_Scrollbar_Y.pack(side=RIGHT, fill=Y)
Order_Scrollbar_X.config(command=Order_List.xview)
Order_Scrollbar_X.pack(side=BOTTOM, fill=X)
Order_List.pack()

# Order button
Order_Btn = Button(Menu_Win, text="Place order", command=Place_Order)
Order_Btn.place(x=117.5, y=530)


# Page_Open(Menu_Win)
Menu_Win.mainloop()
