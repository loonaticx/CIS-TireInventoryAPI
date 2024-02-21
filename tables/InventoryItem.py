from dataclasses import dataclass


@dataclass
class InventoryItem:
    """
    A local "Inventory" object, not dependent on the database.
    """
    brand: str
    model: str = "Colorless"
    loadRating: float = 0.0
    speedRating: float = 0.0
    itemType: str = "No description."
    stockAmt: int = 0
