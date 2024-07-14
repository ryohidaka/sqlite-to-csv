import os
from sqlalchemy import MetaData, Table, select
from sqlite_to_csv.lib.logger import init_logger
from sqlite_to_csv.lib.sqlalchemy import get_all_tables, get_engine


def main() -> int:
    print("Hello from sqlite-to-csv!")

    database = os.environ.get("DB")
    app = SqliteToCSV(database=database)

    app.export()
    return 0


class SqliteToCSV:
    """
    Export data from a SQLite database to CSV files.

    Args:
        database (str): Path to the SQLite database.

    Returns:
        None
    """

    def __init__(
        self,
        database: str,
    ):
        self.logger = init_logger()

        self.engine = get_engine(logger=self.logger, database=database)
        self.connection = self.engine.connect()
        self.metadata = MetaData()

        self.logger.info(f"Initialized SqliteToCSV with database: {database}.")

    def export(self):
        table_names = get_all_tables(engine=self.engine, logger=self.logger)

        for table_name in table_names:
            try:
                self.logger.info(f"Processing table: {table_name}")
                table = Table(table_name, self.metadata, autoload_with=self.engine)
                stmt = select(table)
                results = self.connection.execute(stmt).fetchall()
                print(len(results))

                self.logger.info(f"Successfully processed table: {table_name}")
            except Exception as e:
                self.logger.error(f"Error processing table {table_name}: {e}")
                continue

        self.connection.close()
        self.logger.info("Closed database connection")
