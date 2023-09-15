from tkinter import *
from tkinter import ttk
import backend

window = Tk()
window.title('view transactions')
window.geometry('1020x300')

cols = ('number', 'amount', 'receiver id', 'sender id', 'time')
list1 = ttk.Treeview(window, height=10, columns=cols, show='headings')
for col in cols:
    list1.heading(col, text=col)
list1.grid(row=0, column=0, rowspan=6, columnspan=5)
sb1 = Scrollbar(window)
sb1.grid(row=0, column=6, rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

def clear_list():
    list1.delete(*list1.get_children())

def fill_list(transactions):
    for transaction in transactions:
        list1.insert("", END, values=transaction)

def view_command():
    clear_list()
    transactions = backend.view_transactions()
    fill_list(transactions)

def clear_db():
    backend.truncate_transaction()
    view_command()

b1 = Button(window, text='view All', width=12, command=lambda: view_command())
b1.grid(row=7, column=0)

b2 = Button(window, text='clear db', width=12, command=lambda: clear_db())
b2.grid(row=7, column=1)

window.mainloop()