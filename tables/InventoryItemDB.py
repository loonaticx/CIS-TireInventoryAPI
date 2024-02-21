from sqlalchemy import Column, Integer, String, Float

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
    loadRating = Column(Float)
    speedRating = Column(Float)
    itemType = Column(String(64))
    stockAmt = Column(Integer)

    def __init__(self, inventoryItem: InventoryItem):
        self.brand = inventoryItem.brand
        self.model = inventoryItem.model
        self.loadRating = inventoryItem.loadRating
        self.speedRating = inventoryItem.speedRating
        self.itemType = inventoryItem.itemType
        self.stockAmt = inventoryItem.stockAmt

    def __repr__(self):
        return "<InventoryItemDBEntry(brand='%s', model='%s', stockAmt='%s')>" % (
            self.brand,
            self.model,
            self.stockAmt,
        )
