Chocolate House Seasonal Flavors and Inventory Management
Overview
This project provides a Python-based SQLite database management system for managing seasonal chocolate flavors, inventory, and customer suggestions.

Requirements
Python 3.x
SQLite3
Setup Instructions
Clone or download the repository.
Ensure Python and SQLite3 are installed on your system.
Run chocolatehouse.db file in the same directory as the script, as this is the database file the script will connect to.
Running the Script
To initialize tables, add data, and retrieve information:

Run the script by executing:
bash
Copy code
python <script_name>.py
The script will insert sample seasonal flavors, ingredients, and customer suggestions, and then retrieve and display them.
Database Methods:

add_seasonal_flavor: Adds seasonal chocolate flavors with availability dates.
get_seasonal_flavors: Retrieves all seasonal flavors.
add_ingredient: Adds ingredients with quantity and unit of measurement to inventory.
get_inventory: Fetches all items in inventory.
add_customer_suggestion: Records customer flavor suggestions and allergy concerns.
get_customer_suggestions: Retrieves all customer suggestions.
