from sqlalchemy import Column, Integer, String

from tables.InventoryItem import InventoryItem

from sqlalchemy.orm import declarative_base


class InventoryItemDBEntry(declarative_base()):
    """
    Skeleton for a db entry in the "inventory" table.

    Will be added into the database upon init
    """

    __tablename__ = "inventory"

    id = Column(Integer, primary_key = True, autoincrement = True)
    brand = Column(String(64))
    model = Column(String(64))
    loadRating = Column(Integer)
    speedRating = Column(String(1))
    type = Column(String(64))
    stock = Column(Integer)

    def __init__(self, inventoryItem: InventoryItem):
        self.brand = inventoryItem.brand
        self.model = inventoryItem.model
        self.loadRating = inventoryItem.loadRating
        self.speedRating = inventoryItem.speedRating
        self.type = inventoryItem.itemType
        self.stock = inventoryItem.stockAmt

    def __repr__(self):
        return "<InventoryItemDBEntry(brand='%s', model='%s', stock='%s')>" % (
            self.brand,
            self.model,
            self.stock,
        )
