"""
Generates arbitrary drinks
"""
import random
from dataclasses import dataclass

from base.DatabaseManager import *
from tables.InventoryItem import InventoryItem
from tables.InventoryItemDB import InventoryItemDBEntry
from config.Config import Config


# Not going to cause a big deal if user tries to input a new tire
# with an invalid model name wrt the brand.

# Arbitrary examples

# 30 different outcomes
tire_brand_models = {
    "Michelin": ["Primacy MXM4", "Defender", "Pilot Sport"],
    "Bridgestone": ["Ecopia", "Potenza", "Dueler"],
    "Goodyear": ["Assurance", "Eagle", "Wrangler"],
    "Continental": ["ContiProContact", "ExtremeContact", "TrueContact"],
    "Pirelli": ["P Zero", "Cinturato", "Scorpion"],
    "Firestone": ["Destination LE2", "Transforce HT", "Firehawk Indy 500"],
    "Dunlop": ["SP Sport Maxx", "Direzza DZ102", "Winter Maxx"],
    "Hankook": ["Ventus V12 evo2", "Dynapro AT2", "Winter i*cept evo2"],
    "Yokohama": ["AVID Ascend", "Geolandar A/T G015", "Advantage T/A"],
    "Toyo": ["Proxes Sport", "Open Country A/T III", "Extensa A/S II"],
}

total_tire_count = 0
for mdl in tire_brand_models.values():
    total_tire_count += len(mdl)


# Reference:
# https://www.readingtruck.com/understanding-truck-tires-load-ratings-and-sizes/
# https://www.discounttire.com/learn/speed-rating
speed_ratings = {
    "B": 31,
    "C": 37,
    "D": 40,
    "E": 43,
    "F": 50,
    "G": 56,
    "J": 62,
    "K": 68,
    "L": 75,
    "M": 81,
    "N": 87,
    "P": 93,
    "Q": 99,
    "R": 106,
    "S": 112,
    "T": 116,
    "U": 124,
    "H": 130,
    "V": 149,
    "W": 168,
    "Y": 186,

}

tire_types = [
    "All-Season",
    "Summer",
    "Winter",
    "Performance",
    "Touring",
    "Highway",
    "Off-Road",
    "Mud",
    "All-Terrain",
    "Run-Flat",
    "Low-Profile",
    "Grand Touring",
    "Street/Sport Truck All-Season",
    "Trailer",
]

tireHashes = []

# https://www.bigotires.com/resources/suspension-&-front-end/what-is-tire-load-rating
load_ratings = (71, 110)
@dataclass
class TireGenerator:

    def _generateTireEntry(self) -> InventoryItemDBEntry:
        tireBrand = random.choice(list(tire_brand_models.keys()))
        tireModel = random.choice(tire_brand_models[tireBrand])

        # To generate a unique brand/model...
        # since it looks a bit weird having identical entries with different attributes
        tireHash = hash(f"{tireBrand}_{tireModel}")
        # But if we end up generating over the total tire count, then just let it go
        while tireHash in tireHashes and len(tireHashes) <= total_tire_count:
            tireBrand = random.choice(list(tire_brand_models.keys()))
            tireModel = random.choice(tire_brand_models[tireBrand])
            tireHash = hash(f"{tireBrand}_{tireModel}")

        tireHashes.append(tireHash)

        tireType = random.choice(tire_types)

        tireLoadRating = random.randint(*load_ratings)
        tireSpeedRating = random.choice(list(speed_ratings.keys()))
        tireStock = random.randint(0, 42)
        tire = InventoryItem(
            brand=tireBrand,
            model=tireModel,
            loadRating = tireLoadRating,
            speedRating = tireSpeedRating,
            itemType=tireType,
            stockAmt=tireStock,
        )
        return InventoryItemDBEntry(tire)

    def generateTires(self, tireAmt: int):
        generatedTires = []
        for _ in range(tireAmt):
            generatedTires.append(self._generateTireEntry())
        return generatedTires


if __name__ == "__main__":
    """
    Driver code; when ran, will insert arbitrary drink entries into the database.
    """
    # Generate our DB
    database = DatabaseManager(Config)
    database.initSession()

    tireAmt = 10
    for genTire in TireGenerator().generateTires(tireAmt):
        database.generateEntry(genTire)
    print(f"Generated {tireAmt} tires!")
