from sqlalchemy import Column, Integer, String, Float

from tables.InventoryItem import InventoryItem

from sqlalchemy.orm import declarative_base


class InventoryItemDBEntry(declarative_base()):
    """
    Skeleton for a db entry in the "drinks" table.

    Will be added into the database upon init
    """

    __tablename__ = "inventory"

    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(64))
    price = Column(Float)
    color = Column(String(32), nullable = True)
    description = Column(String(128), nullable = True, default = "No description.")

    def __init__(self, inventoryItem: InventoryItem):
        self.drink = inventoryItem
        self.name = inventoryItem.name
        self.price = inventoryItem.price
        self.color = inventoryItem.color
        self.description = inventoryItem.description

    def __repr__(self):
        return "<InventoryItemDBEntry(name='%s', price='%s', id='%s')>" % (
            self.name,
            self.price,
            self.id,
        )
