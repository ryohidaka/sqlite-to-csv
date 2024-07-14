from logging import Logger
from sqlalchemy import Engine, create_engine, inspect


def get_engine(logger: Logger, database: str, echo: bool = False):
    """
    Create a SQLAlchemy engine.

    Args:
        database (str): Path to the SQLite database.
        echo (bool): Enable SQLAlchemy echo for debugging.

    Returns:
        sqlalchemy.engine.Engine: SQLAlchemy engine instance.
    """
    engine = create_engine(database, echo=echo)
    logger.info(f"Created SQLAlchemy engine for database: {database}")
    return engine


def get_all_tables(engine: Engine, logger: Logger) -> list[str]:
    """
    Get all table names from the database.

    Returns:
        list[str]: List of table names.
    """
    inspector = inspect(engine)
    table_names = inspector.get_table_names()
    logger.info(f"Retrieved table names: {table_names}")
    return table_names
