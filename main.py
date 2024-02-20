"""
This homework requires you to have a remote MySQL database setup.
For this assignment, we will create an inventory management system for a tire store.
Create a table in your existing database named inventory. In this table you need at least
the following columns: id, brand, model, loadrating, speedrating, type, stock. You may
add additional columns if you like

"""
from base.DatabaseManager import DatabaseManager
from tables.InventoryItem import InventoryItem
from tables.InventoryItemDB import InventoryItemDBEntry
from config.Config import Config

# Generate our DB
database = DatabaseManager(Config)
database.initSession()

item = InventoryItemDBEntry(InventoryItem("test", 1.0))
database.generateEntry(item)

