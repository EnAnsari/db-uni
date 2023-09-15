from tkinter import *
import tkinter.messagebox
import backend

window = Tk()
window.title('Transaction')
window.geometry('270x250')

l1 = Label(window, text='Sender Account ID')
l1.grid(row=0, column=0)

l2 = Label(window, text='Receiver Account ID')
l2.grid(row=1, column=0)

l3 = Label(window, text='Amount')
l3.grid(row=2, column=0)

sender_id = StringVar()
e1 = Entry(window, textvariable=sender_id)
e1.grid(row=0, column=1)

receiver_id = StringVar()
e2 = Entry(window, textvariable=receiver_id)
e2.grid(row=1, column=1)

amount_text = StringVar()
e3 = Entry(window, textvariable=amount_text)
e3.grid(row=2, column=1)

def send_money():
    if not amount_text.get().isnumeric():
        tkinter.messagebox.showerror('Error', 'Amount value should be number!')
        return
    try:
        list_of_result = backend.transaction_money(sender_id.get(), receiver_id.get(), int(amount_text.get()))
        if list_of_result[0] != 0:
            tkinter.messagebox.showerror('Error', 'we have an error in data base!')
        else:
            l4.config(text='result: ', font='consolas')
            l5.config(text=f'number of transaction:\n{list_of_result[5]}'
                           f'\n\nSender: {list_of_result[1]} by Amount: {list_of_result[2]}'
                           f'\nReceiver: {list_of_result[3]} by Amount: {list_of_result[4]}'
                           f'\nTime: {backend.datetime.datetime.now()}', font='consolas 10', bg='lightyellow')
    except:
        tkinter.messagebox.showerror('Error', 'an invalid value!')



sendbtn = Button(window, text='Send', bg='lightgreen', width=32, bd=2, command=lambda: send_money())
sendbtn.grid(row=3, column=0, columnspan=2)

l4 = Label(window)
l4.grid(row=4, column=0)

l5 = Label(window)
l5.grid(row=5, column=0, rowspan=2, columnspan=5)

window.mainloop()