# main.py
# The Tkinter GUI of the Smart Canteen Ordering System.
# Run this file to start the program:  python main.py

import tkinter as tk
from tkinter import ttk, messagebox
import database

# The cart is a list. Each item in the cart is a dictionary, for example:
# {"name": "Tea", "price": 10, "quantity": 2, "subtotal": 20}
cart = []


# ---------------------------------------------------------------
# VIEW MENU WINDOW
# ---------------------------------------------------------------
def open_menu_window():
    window = tk.Toplevel(root)
    window.title("Menu")
    window.geometry("350x380")

    tk.Label(window, text="Food Menu", font=("Arial", 16, "bold")).pack(pady=10)

    table = ttk.Treeview(window, columns=("item", "price"), show="headings", height=12)
    table.heading("item", text="Food Item")
    table.heading("price", text="Price (Rs.)")
    table.column("item", width=180)
    table.column("price", width=100, anchor="center")
    table.pack(padx=10, pady=5)

    menu_list = database.get_menu()
    for item_name, price in menu_list:
        table.insert("", "end", values=(item_name, price))


# ---------------------------------------------------------------
# PLACE ORDER WINDOW
# ---------------------------------------------------------------
def open_order_window():
    cart.clear()                          # start with an empty cart
    menu_list = database.get_menu()

    # Make a dictionary: item name -> price  (easy to look up the price)
    price_of = {}
    for item_name, price in menu_list:
        price_of[item_name] = price

    window = tk.Toplevel(root)
    window.title("Place Order")
    window.geometry("520x600")

    tk.Label(window, text="Place Your Order", font=("Arial", 16, "bold")).pack(pady=10)

    # ----- Input area -----
    form = tk.Frame(window)
    form.pack(pady=5)

    tk.Label(form, text="Customer Name:").grid(row=0, column=0, sticky="w", pady=5)
    name_entry = tk.Entry(form, width=25)
    name_entry.grid(row=0, column=1, pady=5)

    tk.Label(form, text="Food Item:").grid(row=1, column=0, sticky="w", pady=5)
    food_box = ttk.Combobox(form, values=list(price_of.keys()), state="readonly", width=22)
    food_box.grid(row=1, column=1, pady=5)

    tk.Label(form, text="Price (Rs.):").grid(row=2, column=0, sticky="w", pady=5)
    price_label = tk.Label(form, text="-")
    price_label.grid(row=2, column=1, sticky="w", pady=5)

    tk.Label(form, text="Quantity:").grid(row=3, column=0, sticky="w", pady=5)
    quantity_entry = tk.Entry(form, width=10)
    quantity_entry.insert(0, "1")
    quantity_entry.grid(row=3, column=1, sticky="w", pady=5)

    # ----- Cart table -----
    cart_table = ttk.Treeview(
        window, columns=("item", "price", "qty", "subtotal"), show="headings", height=9
    )
    cart_table.heading("item", text="Item")
    cart_table.heading("price", text="Price")
    cart_table.heading("qty", text="Qty")
    cart_table.heading("subtotal", text="Subtotal")
    cart_table.column("item", width=180)
    cart_table.column("price", width=80, anchor="center")
    cart_table.column("qty", width=60, anchor="center")
    cart_table.column("subtotal", width=100, anchor="center")

    total_label = tk.Label(window, text="Total Amount: Rs. 0", font=("Arial", 13, "bold"))

    # ----- Functions used by the buttons -----
    def show_price(event=None):
        """Runs when a food item is selected: shows its price."""
        selected_item = food_box.get()
        if selected_item in price_of:
            price_label.config(text=str(price_of[selected_item]))

    def refresh_cart():
        """Redraw the cart table and recalculate the total bill."""
        for row in cart_table.get_children():
            cart_table.delete(row)

        total = 0
        for item in cart:
            cart_table.insert(
                "", "end",
                values=(item["name"], item["price"], item["quantity"], item["subtotal"])
            )
            total = total + item["subtotal"]

        total_label.config(text="Total Amount: Rs. " + str(total))

    def add_to_cart():
        """Runs when 'Add to Cart' is clicked."""
        selected_item = food_box.get()
        quantity_text = quantity_entry.get().strip()

        if selected_item == "":
            messagebox.showwarning("Warning", "Please select a food item.")
            return

        # Check that quantity is a whole number
        try:
            quantity = int(quantity_text)
        except ValueError:
            messagebox.showwarning("Warning", "Quantity must be a whole number.")
            return

        if quantity <= 0 or quantity > 50:
            messagebox.showwarning("Warning", "Quantity must be between 1 and 50.")
            return

        price = price_of[selected_item]

        # If the item is already in the cart, just increase its quantity
        found = False
        for item in cart:
            if item["name"] == selected_item:
                item["quantity"] = item["quantity"] + quantity
                item["subtotal"] = item["quantity"] * item["price"]
                found = True

        if found == False:
            cart.append({
                "name": selected_item,
                "price": price,
                "quantity": quantity,
                "subtotal": price * quantity,
            })

        refresh_cart()
        quantity_entry.delete(0, tk.END)
        quantity_entry.insert(0, "1")

    def clear_all():
        """Runs when 'Clear' is clicked: empties cart and inputs."""
        cart.clear()
        name_entry.delete(0, tk.END)
        food_box.set("")
        price_label.config(text="-")
        quantity_entry.delete(0, tk.END)
        quantity_entry.insert(0, "1")
        refresh_cart()

    def place_order():
        """Runs when 'Place Order' is clicked."""
        customer_name = name_entry.get().strip()

        if customer_name == "":
            messagebox.showwarning("Warning", "Please enter your name.")
            return

        if len(cart) == 0:
            messagebox.showwarning("Warning", "Your cart is empty.")
            return

        order_id, total = database.save_order(customer_name, cart)

        if order_id is None:
            messagebox.showerror("Error", "Could not save the order. Please try again.")
        else:
            messagebox.showinfo(
                "Order Confirmation",
                "Order placed successfully!\n\n"
                "Order ID: " + str(order_id) + "\n"
                "Name: " + customer_name + "\n"
                "Total Amount: Rs. " + str(total)
            )
            clear_all()

    # Link the combobox to show_price
    food_box.bind("<<ComboboxSelected>>", show_price)

    # ----- Buttons and widgets placed on the window -----
    tk.Button(window, text="Add to Cart", width=15, command=add_to_cart).pack(pady=8)

    tk.Label(window, text="Cart", font=("Arial", 12, "bold")).pack()
    cart_table.pack(padx=10, pady=5)
    total_label.pack(pady=8)

    button_frame = tk.Frame(window)
    button_frame.pack(pady=5)
    tk.Button(button_frame, text="Place Order", width=15, command=place_order).grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="Clear", width=15, command=clear_all).grid(row=0, column=1, padx=10)


# ---------------------------------------------------------------
# PREVIOUS ORDERS WINDOW
# ---------------------------------------------------------------
def open_orders_window():
    window = tk.Toplevel(root)
    window.title("Previous Orders")
    window.geometry("560x430")

    tk.Label(window, text="Previous Orders", font=("Arial", 16, "bold")).pack(pady=10)

    table = ttk.Treeview(
        window, columns=("id", "name", "total", "date"), show="headings", height=12
    )
    table.heading("id", text="Order ID")
    table.heading("name", text="Customer")
    table.heading("total", text="Total (Rs.)")
    table.heading("date", text="Date & Time")
    table.column("id", width=70, anchor="center")
    table.column("name", width=140)
    table.column("total", width=90, anchor="center")
    table.column("date", width=170, anchor="center")
    table.pack(padx=10, pady=5)

    orders = database.get_all_orders()
    for order in orders:
        table.insert("", "end", values=order)

    def show_order_items():
        """Show the food items of the order selected in the table."""
        selected = table.selection()
        if len(selected) == 0:
            messagebox.showwarning("Warning", "Please select an order first.")
            return

        row_values = table.item(selected[0])["values"]
        order_id = row_values[0]

        items = database.get_order_items(order_id)
        text = ""
        for item_name, quantity, price, subtotal in items:
            text = text + item_name + "  x " + str(quantity) + "  =  Rs. " + str(subtotal) + "\n"

        messagebox.showinfo("Order " + str(order_id) + " Items", text)

    tk.Button(window, text="View Items of Selected Order", command=show_order_items).pack(pady=8)


# ---------------------------------------------------------------
# MAIN PROGRAM STARTS HERE
# ---------------------------------------------------------------
database.create_tables()
database.add_default_menu()

root = tk.Tk()
root.title("Smart Canteen Ordering System")
root.geometry("420x400")

tk.Label(root, text="SMART CANTEEN\nORDERING SYSTEM", font=("Arial", 20, "bold")).pack(pady=30)

tk.Button(root, text="Place Order", width=25, height=2, command=open_order_window).pack(pady=6)
tk.Button(root, text="View Menu", width=25, height=2, command=open_menu_window).pack(pady=6)
tk.Button(root, text="View Previous Orders", width=25, height=2, command=open_orders_window).pack(pady=6)
tk.Button(root, text="Exit", width=25, height=2, command=root.destroy).pack(pady=6)

root.mainloop()
