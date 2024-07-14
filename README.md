# sqlite2csv

[![PyPI version](https://badge.fury.io/py/sqlite2csv.svg)](https://badge.fury.io/py/sqlite2csv)
![build](https://github.com/ryohidaka/sqlite2csv/workflows/Build/badge.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Export data from a SQLite database to CSV files.

## Installation

You can install this library using PyPI:

```shell
pip install sqlite2csv
```

## Usage

### Retrieve all tables

```python
from sqlite2csv import SqliteToCSV

database = "sqlite:///db/test.db"
dest_dir = ".output"

app = SqliteToCSV(database=database, dest_dir=dest_dir)
app.export()
```

### Retrieve an arbitrary tables

```python
from sqlite2csv import SqliteToCSV

database = "sqlite:///db/test.db"
dest_dir = ".output"
table_names = ["users", "projects"]

app = SqliteToCSV(database=database, dest_dir=dest_dir, table_names=table_names)
app.export()
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
