from sqlite_to_csv.lib.logger import init_logger


def main() -> int:
    print("Hello from sqlite-to-csv!")
    app = SqliteToCSV()
    return 0


class SqliteToCSV:
    """
    Export data from a SQLite database to CSV files.
    """

    def __init__(
        self,
    ):
        self.logger = init_logger()
