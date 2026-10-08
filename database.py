# database.py
# This file handles everything related to the SQLite database.
# main.py never writes SQL - it only calls the functions from this file.

import sqlite3
from datetime import datetime

DB_NAME = "canteen.db"


def connect_database():
    """Open a connection to the database file (created if it does not exist)."""
    con = sqlite3.connect(DB_NAME)
    return con


def create_tables():
    """Create the 3 tables if they are not already there."""
    con = connect_database()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            price INTEGER NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            total_amount INTEGER NOT NULL,
            order_date TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price INTEGER NOT NULL,
            subtotal INTEGER NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders (order_id)
        )
    """)

    con.commit()   # save the changes permanently
    con.close()


def add_default_menu():
    """Put some food items in the menu table (only if the menu is empty)."""
    con = connect_database()
    cur = con.cursor()

    cur.execute("SELECT COUNT(*) FROM menu")
    count = cur.fetchone()[0]          # fetchone() gives one row, [0] is the first value

    if count == 0:
        default_items = [
            ("Samosa", 15),
            ("Vada Pav", 20),
            ("Sandwich", 40),
            ("Veg Burger", 50),
            ("Masala Dosa", 60),
            ("Pav Bhaji", 70),
            ("Tea", 10),
            ("Coffee", 20),
            ("Cold Drink", 30),
        ]
        for item in default_items:
            cur.execute("INSERT INTO menu (item_name, price) VALUES (?, ?)", item)
        con.commit()

    con.close()


def get_menu():
    """Return all menu items as a list of (item_name, price)."""
    con = connect_database()
    cur = con.cursor()
    cur.execute("SELECT item_name, price FROM menu ORDER BY id")
    menu_list = cur.fetchall()         # fetchall() gives ALL rows as a list
    con.close()
    return menu_list


def save_order(customer_name, cart):
    """
    Save one order.
    cart is a list of dictionaries like:
        {"name": "Tea", "price": 10, "quantity": 2, "subtotal": 20}
    Returns (order_id, total) if saved, or (None, 0) if something went wrong.
    """
    total = 0
    for item in cart:
        total = total + item["subtotal"]

    order_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    try:
        con = connect_database()
        cur = con.cursor()

        # Step 1: save the main order
        cur.execute(
            "INSERT INTO orders (customer_name, total_amount, order_date) VALUES (?, ?, ?)",
            (customer_name, total, order_date)
        )
        order_id = cur.lastrowid       # the order_id SQLite just created

        # Step 2: save every cart item, linked with the same order_id
        for item in cart:
            cur.execute(
                "INSERT INTO order_items (order_id, item_name, quantity, price, subtotal) "
                "VALUES (?, ?, ?, ?, ?)",
                (order_id, item["name"], item["quantity"], item["price"], item["subtotal"])
            )

        con.commit()
        con.close()
        return order_id, total

    except sqlite3.Error as error:
        print("Database error:", error)
        return None, 0


def get_all_orders():
    """Return all orders, newest first."""
    con = connect_database()
    cur = con.cursor()
    cur.execute(
        "SELECT order_id, customer_name, total_amount, order_date "
        "FROM orders ORDER BY order_id DESC"
    )
    orders = cur.fetchall()
    con.close()
    return orders


def get_order_items(order_id):
    """Return the food items of one order."""
    con = connect_database()
    cur = con.cursor()
    cur.execute(
        "SELECT item_name, quantity, price, subtotal FROM order_items WHERE order_id = ?",
        (order_id,)
    )
    items = cur.fetchall()
    con.close()
    return items
