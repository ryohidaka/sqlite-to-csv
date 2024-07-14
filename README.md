# sqlite-to-csv

[![PyPI version](https://badge.fury.io/py/sqlite-to-csv.svg)](https://badge.fury.io/py/sqlite-to-csv)
![build](https://github.com/ryohidaka/sqlite-to-csv/workflows/Build/badge.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Export data from a SQLite database to CSV files.

## Installation

You can install this library using PyPI:

```shell
pip install sqlite-to-csv
```

## Usage

### Retrieve all tables

```python
from sqlite_to_csv import SqliteToCSV

database = "sqlite:///db/test.db"
dest_dir = ".output"

app = SqliteToCSV(database=database, dest_dir=dest_dir)
app.export()
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
