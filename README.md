# coffee-shop-challenge

# ☕ Coffee Orders – Python OOP Lab

A simple object-oriented program modeling customers, coffees, and orders at a coffee shop. Built to practice object relationships, encapsulation, and basic data handling in Python.

---

## 📁 Project Structure

project/
│
├── customer.py # Defines the Customer class
├── coffee.py # Defines the Coffee class
├── order.py # Defines the Order class
└── main.py # (Optional) Used for testing and running the app

markdown
Copy
Edit

---

## 📌 Features

### Customer
- `name` property (1–15 character string)
- `create_order(coffee, price)` — Creates an order linked to the customer
- `orders()` — Returns all orders for that customer
- `coffees()` — Unique coffees the customer has ordered

### Coffee
- `name` property (minimum 3 characters, read-only)
- `orders()` — Returns all orders for that coffee
- `customers()` — Unique customers who ordered that coffee
- `num_orders()` — Count of all orders for this coffee
- `average_price()` — Average price of this coffee’s orders

### Order
- Links a customer and a coffee
- Has a price (float between 1.0 and 10.0)
- Properties: `customer`, `coffee`, `price`

---

## 🛠️ How to Use

1. Clone the repo or download the files.
2. Run the program using a `main.py` or in a Python shell:
   ```bash
   python main.py
You can create instances and test like this:

python
Copy
Edit
from customer import Customer
from coffee import Coffee
from order import Order

alice = Customer("Alice")
latte = Coffee("Latte")

alice.create_order(latte, 4.5)

print(alice.orders())         # List of Order instances
print(alice.coffees())        # [latte]
print(latte.num_orders())     # 1
print(latte.average_price())  # 4.5
✅ Requirements
Python 3.7+

No external libraries required

🧠 Learning Objectives
Understand and apply object relationships (association, aggregation)

Use class methods, instance methods, and property decorators

Maintain clear logic and separation of concerns across files

🚧 To-Do
Add basic CLI or menu interaction

Implement persistence (saving data to a file)

Add unit tests

vbnet
Copy
Edit

Let me know if you'd like help writing a `main.py` for quick testing or want this saved as a downloadable file.









