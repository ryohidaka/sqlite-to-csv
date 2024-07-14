import os
import pandas as pd
from sqlalchemy import MetaData, Table, select
from sqlite2csv.lib.logger import init_logger
from sqlite2csv.lib.pandas import write_csv
from sqlite2csv.lib.sqlalchemy import get_all_tables, get_engine


def main() -> int:
    print("Hello from sqlite2csv!")

    database = os.environ.get("DB")
    dest_dir = ".output"
    app = SqliteToCSV(database=database, dest_dir=dest_dir, debug=True)

    app.export()
    return 0


class SqliteToCSV:
    """
    Export data from a SQLite database to CSV files.

    Args:
        database (str): Path to the SQLite database.
        dest_dir (str): Path to export csv.
        table_names (list[str], optional): List of table names to export. If None, all tables will be exported.
        debug (bool): Enable SQLAlchemy echo for debugging.

    Returns:
        None
    """

    def __init__(
        self,
        database: str,
        dest_dir: str,
        table_names: list[str] = None,
        debug: bool = False,
    ):
        self.logger = init_logger()

        self.engine = get_engine(logger=self.logger, database=database, echo=debug)
        self.connection = self.engine.connect()
        self.metadata = MetaData()

        self.dest_dir = dest_dir
        self.table_names = table_names

        self.logger.info(
            f"Initialized SqliteToCSV with database: {database}, dest_dir: {dest_dir}, table_names: {table_names}, debug: {debug}"
        )

    def export(self):
        if not self.table_names:
            self.table_names = get_all_tables(engine=self.engine, logger=self.logger)
            self.logger.info(f"Retrieved all table names: {self.table_names}")

        # Collect data from tables
        data_frames = {}

        for table_name in self.table_names:
            try:
                self.logger.info(f"Processing table: {table_name}")
                table = Table(table_name, self.metadata, autoload_with=self.engine)
                stmt = select(table)
                results = self.connection.execute(stmt).fetchall()
                df = pd.DataFrame(
                    results, columns=[column.name for column in table.columns]
                )
                data_frames[table_name] = df

                self.logger.info(f"Successfully processed table: {table_name}")
            except Exception as e:
                self.logger.error(f"Error processing table {table_name}: {e}")
                continue

        # Write data to CSV
        for table_name, df in data_frames.items():
            write_csv(
                df, dest_dir=self.dest_dir, filename=table_name, logger=self.logger
            )

        self.connection.close()
        self.logger.info("Closed database connection")
