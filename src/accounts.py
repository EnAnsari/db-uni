from tkinter import *
import tkinter.messagebox
import backend

window = Tk()
window.title('Accounts')
window.geometry('400x200')


l1 = Label(window, text='Account ID')
l1.grid(row=0, column=0)

l2 = Label(window, text='username')
l2.grid(row=0, column=2)

l3 = Label(window, text='password')
l3.grid(row=1, column=0)

l4 = Label(window, text='Amount')
l4.grid(row=1, column=2)

# --------------------- Entries ---------------------------

account_id_text = StringVar()
e1 = Entry(window, textvariable=account_id_text)
e1.grid(row=0, column=1)

username_text = StringVar()
e2 = Entry(window, textvariable=username_text)
e2.grid(row=0, column=3)

password_text = StringVar()
e3 = Entry(window, textvariable=password_text)
e3.grid(row=1, column=1)

amount_text = StringVar()
e4 = Entry(window, textvariable=amount_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, width=35, height=6)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


def get_select_row(event):
    global selected_account
    if len(list1.curselection()) > 0:
        id = list1.curselection()[0]
        selected_account = list1.get(id)
        e1.delete(0, END)
        e1.insert(END, selected_account[0])
        e2.delete(0, END)
        e2.insert(END, selected_account[1])
        e3.delete(0, END)
        e3.insert(END, selected_account[2])
        e4.delete(0, END)
        e4.insert(END, selected_account[3])

#
list1.bind("<<ListboxSelect>>", get_select_row)

#
def clear_list():
    list1.delete(0, END)


def fill_list(accounts):
    for account in accounts:
        list1.insert(END, account)

# def view_command():
#     list1.delete(0, END)
#     accounts = backend.view()
#     for account in accounts:
#         list1.insert(END, account)

def view_command():
    clear_list()
    accounts = backend.view_accounts()
    fill_list(accounts)

def search_command():
    clear_list()
    temp = 0
    if amount_text.get():
        temp = int(amount_text.get())
    else:
        temp = 0
    accounts = backend.search_account(account_id_text.get(), username_text.get(), password_text.get(), temp)
    fill_list(accounts)

def add_command():
    if account_id_text.get() and username_text.get() and password_text.get() and amount_text.get():
        backend.insert_account(account_id_text.get(), username_text.get(), password_text.get(), int(amount_text.get()))
        view_command()

def delete_command():
    try:
        # print(selected_account[0])
        backend.delete_account(selected_account[0])
        view_command()
    except:
        tkinter.messagebox.showerror('Error', 'You dont select any thing!')

def update_command():
    try:
        backend.update_account(selected_account[0], account_id_text.get(), username_text.get(), password_text.get(), int(amount_text.get()))
        view_command()
    except:
        tkinter.messagebox.showerror('Error', 'You dont select any thing!')


b1 = Button(window, text='view All', width=12, command=lambda: view_command())
b1.grid(row=2, column=3)
#
b2 = Button(window, text='Search Entry', width=12, command=lambda: search_command())
b2.grid(row=3, column=3)
#
b3 = Button(window, text='Add Entry', width=12, command=lambda: add_command())
b3.grid(row=4, column=3)
#
b4 = Button(window, text='Update Entry', width=12, command=lambda: update_command())
b4.grid(row=5, column=3)
#
b5 = Button(window, text='Delete Selected', width=12, command=lambda: delete_command())
b5.grid(row=6, column=3)
#
b6 = Button(window, text='Close', width=12, command=window.destroy)
b6.grid(row=7, column=3)


window.mainloop()