import random
import sqlite3
import datetime
import uuid

def connect():
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS customer(
            id text PRIMARY KEY,
            name text, email text
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS account(
            account_id text PRIMARY KEY,
            username text UNIQUE, password text,
            amount INTEGER
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ownership(
            customer_id text,
            account_id text,
            PRIMARY KEY (customer_id, account_id)
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS credit_card(
            number text PRIMARY KEY,
            first_password text,
            second_password text,
            cvc_code text,
            expiration_date date
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS card_connect(
            account_id text,
            card_number text,
            PRIMARY KEY (card_number, account_id)
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
            number_ text PRIMARY KEY,
            amount INTEGER,
            receiver_id text, sender_id text, time_ text
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS operator(
            number text PRIMARY KEY,
            address text, type text
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS pay(
            account_id text,
            operation_number text,
            transaction_number text,
            PRIMARY KEY (transaction_number, operation_number, account_id)
        )
    """)
    conn.commit()
    conn.close()

def insert_customer(id, name, email):
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO customer VALUES(?, ?, ?)",
        (id, name, email)
    )
    conn.commit()
    conn.close()

def insert_account(id, username, password, amount):
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO account VALUES(?, ?, ?, ?)",
        (id, username, password, amount)
    )
    conn.commit()
    conn.close()

def view_accounts():
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM account")
    rows = cur.fetchall()
    conn.close()
    return rows

def search_account(id="", username="", password="", amount=0):
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM account WHERE account_id=? OR username=? OR password=? OR amount=?",
        (id, username, password, amount)
    )
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_account(id):
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM account WHERE account_id=?", (id,))
    conn.commit()
    conn.close()

def update_account(selected_id, id, username, password, amount):
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    cur.execute(
        "UPDATE account SET account_id=?, username=?, password=?, amount=? WHERE account_id=?",
        (id, username, password, amount, selected_id)
    )
    conn.commit()
    conn.close()

def transaction_money(sender_id, receiver_id, amount):
    result = []
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    try:
        cur.execute(
            "UPDATE account SET amount = amount - ? WHERE account_id=?",
            (amount, sender_id)
        )
        cur.execute(
            "UPDATE account SET amount = amount + ? WHERE account_id=?",
            (amount, receiver_id)
        )
        result.append(0)
        unique_id = str(uuid.uuid4())
        cur.execute(
            "INSERT INTO transactions VALUES(?, ?, ?, ?, ?)",
            (unique_id, amount, receiver_id, sender_id, str(datetime.datetime.now()))
        )
        print('done')
        cur.execute(
            "SELECT username, amount FROM account WHERE account_id=?",
            (sender_id,)
        )
        sender = cur.fetchall()
        cur.execute(
            "SELECT username, amount FROM account WHERE account_id=?",
            (receiver_id,)
        )
        receiver = cur.fetchall()
        result.append(sender[0][0])
        result.append(sender[0][1])
        result.append(receiver[0][0])
        result.append(receiver[0][1])
        result.append(unique_id)
    except:
        result.append(1)
    conn.commit()
    conn.close()

    return result

def view_transactions():
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM transactions")
    rows = cur.fetchall()
    conn.close()
    return rows

def truncate_transaction():
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM transactions WHERE 1=1")
    conn.commit()
    conn.close()

connect()