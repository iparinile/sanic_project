from sqlalchemy import create_engine

from context import Context
from db.database import DataBase


def init_db_sqlite(contex: Context):
    uri = r'sqlite:///db.sqlite'
    engine = create_engine(
        uri,
        pool_pre_ping=True,
    )
    database = DataBase(connection=engine)
    database.check_connection()

    contex.set('database', database)