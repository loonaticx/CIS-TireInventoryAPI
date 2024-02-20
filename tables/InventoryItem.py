from dataclasses import dataclass


@dataclass
class InventoryItem:
    """
    A local "Inventory" object, not dependent on the database.
    """
    name: str
    price: float
    color: str = "Colorless"
    description: str = "No description."
