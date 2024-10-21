from ..interface.interface_database import DatabaseInterface
from config.config_manager import *
from services.checking.checker import *

from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    select,
    insert,
    update,
    delete,
    and_
)
import os


class SQLiteConnector(DatabaseInterface):
    SQLITE_PATH = os.path.join(preset.folder.database, preset.file.sqlite)

    def __init__(self, database_path=SQLITE_PATH):
        self.engine = create_engine(f"sqlite:///{database_path}")
        self.connection = None
        self.metadata = MetaData()

        # Örnek tablo
        self.sample_table = Table(
            "table_name",
            self.metadata,
            Column("id", Integer, primary_key=True),
            Column("name", String),
            Column("value", String),
        )

        self.metadata.create_all(self.engine)


    # Baglantiyi baslatir
    def connect(self):
        self.connection = self.engine.connect()

    #  Baglantiyi sonlandirir
    def close(self):
        self.connection.close()

    # 'data' bir sozluk olmali, ornegin: {'name': 'example', 'value': '123'}
    def insert(self, data):
        ins_query = insert(self.sample_table).values(data)
        self.connection.execute(ins_query)

    # 'conditions' ve 'new_values' sozlukler olmali
    def update(self, conditions, new_values):
        where_clause = [getattr(self.sample_table.c, key) == value for key, value in conditions.items()]
        upd_query = update(self.sample_table).where(and_(*where_clause)).values(new_values)
        self.connection.execute(upd_query)

    # 'conditions' bir sözlük olmalı
    def delete(self, conditions):
        where_clause = [getattr(self.sample_table.c, key) == value for key, value in conditions.items()]
        del_query = delete(self.sample_table).where(and_(*where_clause))
        self.connection.execute(del_query)

    # 'conditions' bir sozlok olabilir, eger yoksa tum verileri dondurur
    def select(self, conditions=None):
        if conditions:
            where_clause = [getattr(self.sample_table.c, key) == value for key, value in conditions.items()]
            sel_query = select(self.sample_table).where(and_(*where_clause))
        else:
            sel_query = select(self.sample_table)

        result = self.connection.execute(sel_query)
        return result.fetchall()