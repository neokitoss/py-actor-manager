import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name, table_name):
        self.table_name = table_name
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)

    def create(self, first_name, last_name):
        self.connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name,)
        )
        self.connection.commit()

    def all(self):
        actor_manager_cursor = self.connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in actor_manager_cursor
        ]

    def update(self, pk, new_first_name, new_last_name):
        self.connection.execute(
            f"UPDATE {self.table_name}"
            " SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self.connection.commit()

    def delete(self, pk):
        self.connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (pk,)
        )
        self.connection.commit()

