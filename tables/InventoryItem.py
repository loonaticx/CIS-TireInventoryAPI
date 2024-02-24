from dataclasses import dataclass


@dataclass
class InventoryItem:
    """
    A local "Inventory" object, not dependent on the database.
    """
    brand: str = "Tire Brand"
    model: str = "Tire Model"
    loadRating: int = 0
    speedRating: str = ""
    itemType: str = "Tire Type"
    stockAmt: int = 0

