
# A store that stores the following information of the books:
# Author, Title, ISBN, Year
# The user can:
# View all records, Search an entry, Add/Update/Delete any entry, Close

from tkinter import *
from turtle import width
import Backend_BS

window = Tk()

# Connecting Backend to Friontend

# getting the data from user click
def CB_func(event):
    try:
        global selected_tuple # we can call the global variable outside of the function
        index = List1.curselection()[0] # Return the indices of currently selected item.
        selected_tuple = List1.get(index)
        # print(index)
        E1.delete(0,END)
        E1.insert(END, selected_tuple[1])
        E2.delete(0,END)
        E2.insert(END, selected_tuple[2])
        E3.delete(0,END)
        E3.insert(END, selected_tuple[3])
        E4.delete(0,END)
        E4.insert(END, selected_tuple[4])
    except IndexError:
        pass

#View
def view_func():
    List1.delete(0,END)
    for rows in Backend_BS.view():
        List1.insert(END,rows) # Insert ELEMENTS at INDEX with END method

# Search
def search_func():
    List1.delete(0,END)
    for rows in Backend_BS.search(title_text.get(), author_text.get(),year_text.get(),isbn_text.get()):
        List1.insert(END,rows) # Insert ELEMENTS at INDEX with END method


# Add Entry
def add_func():
    Backend_BS.insert(title_text.get(), author_text.get(),year_text.get(),isbn_text.get())
    # the entry needs to be shown in the listbox
    List1.delete(0,END)
    List1.insert(END,(title_text.get(), author_text.get(),year_text.get(),isbn_text.get()))

# Update
def update_func():
        Backend_BS.Update(selected_tuple[0],title_text.get(), author_text.get(),year_text.get(),isbn_text.get())
        List1.delete(0,END)
        for rows in Backend_BS.view():
            List1.insert(END,rows) # Insert ELEMENTS at INDEX with END method

# Delete
def delete_func():
    Backend_BS.delete(selected_tuple[0])
    # to view the updated list
    List1.delete(0,END)
    for rows in Backend_BS.view():
        List1.insert(END,rows) # Insert ELEMENTS at INDEX with END method


L1 = Label(window, text = 'Title')
L1.grid(row = 0 , column=0)
L2 = Label(window, text = 'Author')
L2.grid(row = 0 , column=2)
L3 = Label(window, text = 'Year')
L3.grid(row = 1 , column=0)
L4 = Label(window, text = 'ISBN')
L4.grid(row = 1 , column=2)

# first Entry by the user
title_text = StringVar() # Construct a string variable
E1 = Entry(window, textvariable= title_text)
E1.grid(row = 0 , column=1)

# Second Entry by the user
author_text = StringVar() # Construct a string variable
E2 = Entry(window, textvariable= author_text)
E2.grid(row = 0 , column=3)

# Third Entry by the user
year_text = StringVar() # Construct a string variable
E3 = Entry(window, textvariable= year_text)
E3.grid(row = 1 , column=1)

# Fourth Entry by the user
isbn_text = StringVar() # Construct a string variable
E4 = Entry(window, textvariable= isbn_text)
E4.grid(row = 1 , column=3)

# display a list of items from which a user can select a number of items
List1 = Listbox(window,width=50, height= 6)
List1.grid(row = 2 , column = 0, rowspan=6,columnspan=2) #expand the column and row

# Create the scroll bar
scrlbr = Scrollbar(window)
scrlbr.grid(row = 2 , column = 2, rowspan=6)
# to allow the user to scroll the listbox vertically, 
# we need to link the listbox widget to a vertical scrollbar
List1.configure(yscrollcommand=scrlbr.set) # Set the fractional values of the slider position 
scrlbr.configure(command=List1.yview)

# Bind a function to the widget whenever an event occurs 
List1.bind("<<ListboxSelect>>", CB_func) # When the user selects an item, 
# either with a mouse click or with the arrow keys, a virtual <ListboxSelect> event is generated. 
# You can bind to it to a callback function(CB_func)



# Create the buttons
B1 = Button(window, text= 'View All', width=12, command= view_func)
B1.grid(row = 2 , column = 3)

B2 = Button(window, text= 'Search Entry', width=12, command= search_func)
B2.grid(row = 3 , column = 3)

B3 = Button(window, text= 'Add Entry', width=12, command= add_func)
B3.grid(row = 4 , column = 3)

B4 = Button(window, text= 'Update', width=12, command=update_func) 
B4.grid(row = 5 , column = 3)

B5 = Button(window, text= 'Delete', width=12, command=delete_func)
B5.grid(row = 6 , column = 3)

B6 = Button(window, text= 'Close', width=12, command= window.destroy)
B6.grid(row = 7 , column = 3)

window.mainloop()
