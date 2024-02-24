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
from flask import Flask, jsonify, request, Response

app = Flask(__name__)

# Generate our DB
database = DatabaseManager(Config)
database.initSession()

item = InventoryItemDBEntry(InventoryItem("test"))
database.generateEntry(item)

_tireDB = database.session.query(InventoryItemDBEntry)
_allTires = _tireDB.all()

from sqlalchemy import inspect

mapper = inspect(InventoryItemDBEntry)
attr = mapper.attrs
keys = attr.keys()


@app.route('/api/inventory', methods = ['GET'])
def all_tires():
    # Fetch all entries
    tireDict = database.getTableContents(InventoryItemDBEntry)
    return jsonify(tireDict, content_type = 'application/json')


@app.route('/api/inventory/<tireid>', methods = ['GET'])
def get_tire(tireid):
    # Fetch all entries
    t = _tireDB.get(tireid)

    tireDict = database.getTableContents(InventoryItemDBEntry)
    print(f"k = {t}")
    print(f"why =- {tireDict.get(1)}")
    print(f"id = {tireDict.get(int(tireid))}")
    return jsonify(tireDict.get(int(tireid)), content_type = 'application/json')


# @app.route('/api/inventory/<tireid>', methods=['POST'])
# def change_tire(tire_id):
#     tireDict = database.getTableContents(InventoryItemDBEntry)

# Endpoint for updating a guide
@app.route("/api/inventory/<tireid>", methods = ["PUT"])
def update_tire(tireid):
    print(f"lol {request.args.get('brand')}")
    tireDict = database.getTableContents(InventoryItemDBEntry)
    # print(database.session.query(InventoryItemDBEntry))
    tire = tireDict.get(int(tireid))
    tireDbEntry = _tireDB.filter_by(id = int(tireid)).first()
    print(f"t = {tire}")
    request.get_json(force = True)
    input_brand = request.json['brand']
    tireDbEntry.brand = input_brand
    database.session.commit()

    return jsonify(tire)


app.run('localhost', debug = True)
