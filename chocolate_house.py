import sqlite3
def get_db_connection():
    conn = sqlite3.connect('chocolatehouse.db')  
    conn.row_factory = sqlite3.Row 
    return conn

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

def add_seasonal_flavor(name, description, available_from, available_until):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO seasonal_flavors (name, description, available_from, available_until)
        VALUES (?, ?, ?, ?)''',(name, description, available_from, available_until))

    conn.commit()
    conn.close()

def get_seasonal_flavors():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM seasonal_flavors')
    flavors = cursor.fetchall()

    conn.close()
    return flavors

def add_ingredient(ingredient_name, quantity, unit):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO inventory (ingredient_name, quantity, unit)
        VALUES (?, ?, ?)
    ''', (ingredient_name, quantity, unit))

    conn.commit()
    conn.close()

def get_inventory():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM inventory')
    inventory = cursor.fetchall()

    conn.close()
    return inventory


def add_customer_suggestion(customer_name, flavor_suggestion, allergy_concern):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO customer_suggestions (customer_name, flavor_suggestion, allergy_concern)
        VALUES (?, ?, ?)
    ''', (customer_name, flavor_suggestion, allergy_concern))

    conn.commit()
    conn.close()

def get_customer_suggestions():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM customer_suggestions')
    suggestions = cursor.fetchall()

    conn.close()
    return suggestions

if __name__ == '__main__':
 
    add_seasonal_flavor("Pumpkin Spice", "A seasonal fall flavor with cinnamon and nutmeg", "2024-10-01", "2024-11-30")
    add_seasonal_flavor("Peppermint Bark", "A festive peppermint and chocolate combination", "2024-12-01", "2024-12-31")
    
    add_ingredient("Cocoa Powder", 500, "grams")
    add_ingredient("Peppermint Extract", 200, "ml")

    add_customer_suggestion("Ramesh", "Gingerbread Chocolate", "Gluten-free")
    add_customer_suggestion("Suresh", "Peppermint Chocolate", "None")
    print("\nSeasonal Flavors:")
    for flavor in get_seasonal_flavors():
        
        print(f"{flavor['name']} - {flavor['description']} (Available: {flavor['available_from']} to {flavor['available_until']})")
    
    print("\nInventory:")
    for item in get_inventory():
        print(f"{item['ingredient_name']} - {item['quantity']} {item['unit']}")
    
    print("\nCustomer Suggestions:")
    for suggestion in get_customer_suggestions():
        print(f"{suggestion['customer_name']} suggested {suggestion['flavor_suggestion']} with allergy concern: {suggestion['allergy_concern']}")