from dataclasses import dataclass

from base.ConnectionType import ConnectionType


@dataclass
class Config:
    REMOTE_USERNAME: str = "admin"
    REMOTE_PASSWORD: str = "***REMOVED***"
    REMOTE_HOST: str = "***REMOVED***"
    SCHEMA: str = "InventoryDatabase"

    # Will output active transactions being made to the database in console
    VERBOSE_OUTPUT: bool = True

    # LOCAL_FILE, LOCAL_MEMORY, REMOTE_SERVER
    CONNECTION_MODE: ConnectionType = ConnectionType.LOCAL_FILE

    LOCAL_FILENAME: str = "data.db"
