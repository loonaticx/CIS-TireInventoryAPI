"""
DatabaseManager is the kickstart engine for connecting and working with the database.
"""

import sqlalchemy as db

from sqlalchemy import create_engine, update
from sqlalchemy.engine import URL
from sqlalchemy.sql import text

from base.ConnectionType import ConnectionType
import sys
from sqlalchemy.orm import sessionmaker

from tables.InventoryItemDB import InventoryItemDBEntry

global initialized
initialized = False


class DatabaseManager:

    _tableContentData = {
        InventoryItemDBEntry: {}
    }  # dbEntry : itemDict

    def __init__(self, config):
        global initialized
        if initialized:
            raise Exception("Can't initialize DatabaseManager more than once!")
        self._config = config
        self.session = None
        self.engine = None

    def initSession(self):
        global initialized
        if self._config.CONNECTION_MODE == ConnectionType.LOCAL_MEMORY:
            self.engine = create_engine("sqlite:///:memory:", echo = self._config.VERBOSE_OUTPUT)
        elif self._config.CONNECTION_MODE == ConnectionType.LOCAL_FILE:
            self.engine = create_engine(f"sqlite:///{self._config.LOCAL_FILENAME}", echo = self._config.VERBOSE_OUTPUT)
        elif self._config.CONNECTION_MODE == ConnectionType.REMOTE_SERVER:
            url_object = URL.create(
                "mysql+mysqldb",
                username = self._config.REMOTE_USERNAME,
                password = self._config.REMOTE_PASSWORD,
                host = self._config.REMOTE_HOST,
                database = self._config.SCHEMA,
            )
            # For "production", do not echo to output regardless if we have verbose mode on or not.
            self.engine = create_engine(url_object, echo = False)
        else:
            print("ERROR: Config value CONNECTION_MODE is not recognized. Check your config file!")
            sys.exit()

        self.session = sessionmaker(bind = self.engine)()

        if self._config.VERBOSE_OUTPUT:
            print(f"Connected via {self._config.CONNECTION_MODE}")

        initialized = True

    def generateEntry(self, dbEntry):
        # Creates the table if not done so already
        dbEntry.metadata.create_all(self.engine)
        self.session.add(dbEntry)
        self.session.commit()

        self._tableContentData[dbEntry] = dict()

    # @property
    # def tableContentData(self):
    #     for tableDbEntry in self._tableContentData.keys():
    #         self._tableContentData[tableDbEntry] = self.getTableContents(tableDbEntry)
    #     return self._tableContentData

    # @tableContentData.setter
    # def tableContentData(self, dbEntry):
    #     dbVal = self.getTableContents(dbEntry)
    #     self.tableContentData[dbEntry] = dbVal

    def getTableContents(self, dbEntry):
        tableEntry = self.session.query(dbEntry).all()
        attributes = [attr for attr in dbEntry.__table__.columns.keys()]
        itemDict = dict()
        for item in tableEntry:
            itemEntry = {attr: getattr(item, attr) for attr in attributes}
            itemId = itemEntry.pop('id')
            itemDict[itemId] = itemEntry
        # if not self._tableContentData[dbEntry]:
        #     self._tableContentData[dbEntry] = itemDict
        return itemDict


if __name__ == "__main__":
    from config.Config import Config

    testDB = DatabaseManager(Config)
    testDB.initSession()
