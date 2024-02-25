from dataclasses import dataclass


@dataclass
class InventoryItem:
    """
    A local "Inventory" object, not dependent on the database.
    """
    brand: str = "Unknown Brand"
    model: str = "Unknown Model"
    loadRating: int = 0
    speedRating: str = ""
    itemType: str = "Unknown Type"
    stockAmt: int = 0
