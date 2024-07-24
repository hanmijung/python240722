import sqlite3
import random
import string

class ElectronicsDatabase:
    def __init__(self, db_name='electronics.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS products (
                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 name TEXT NOT NULL,
                                 price REAL NOT NULL)''')

    def insert_product(self, name, price):
        with self.conn:
            self.conn.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))

    def update_product(self, product_id, name=None, price=None):
        with self.conn:
            if name and price:
                self.conn.execute('UPDATE products SET name = ?, price = ? WHERE id = ?', (name, price, product_id))
            elif name:
                self.conn.execute('UPDATE products SET name = ? WHERE id = ?', (name, product_id))
            elif price:
                self.conn.execute('UPDATE products SET price = ? WHERE id = ?', (price, product_id))

    def delete_product(self, product_id):
        with self.conn:
            self.conn.execute('DELETE FROM products WHERE id = ?', (product_id,))

    def select_product(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
        return cursor.fetchone()

    def select_all_products(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM products')
        return cursor.fetchall()

    def generate_sample_data(self, num_samples=100):
        for _ in range(num_samples):
            name = 'Product ' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            price = round(random.uniform(10, 1000), 2)
            self.insert_product(name, price)

# Usage
db = ElectronicsDatabase()

# Generate 100 sample data entries
db.generate_sample_data()

# Insert a new product
db.insert_product('New Product', 99.99)

# Update a product
db.update_product(1, name='Updated Product', price=199.99)

# Delete a product
db.delete_product(2)

# Select a single product
product = db.select_product(3)
print(product)

# Select all products
all_products = db.select_all_products()
print(all_products)
