from sqlalchemy import create_engine 
import pypyodbc as odbc
from sqlalchemy.engine import URL

DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = 'sql_container'
DATABASE_NAME = 'msdb'
PWD = 'Testpassword12'

connection_string = f"""
DRIVER={{{DRIVER_NAME}}};
SERVER={SERVER_NAME};
DATABASE={DATABASE_NAME};
uid=sa;
pwd={PWD};
"""

class EngineConnection:
    _instance = None

    @staticmethod
    def get_instance():
        if EngineConnection._instance is None:
            EngineConnection._instance = EngineConnection()
        return EngineConnection._instance

    def __init__(self):
        if EngineConnection._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            # Create a SQLAlchemy engine using the connection string
            connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
            self.engine = create_engine(connection_url, module=odbc)

# Initialize the singleton instance
EngineConnection.get_instance()

