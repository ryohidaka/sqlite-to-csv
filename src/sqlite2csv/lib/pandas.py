from logging import Logger
import pandas as pd


def write_csv(df: pd.DataFrame, dest_dir: str, filename: str, logger: Logger):
    """
    Write a DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): DataFrame to write.
        filename (str): Name of the output CSV file (without extension).

    Returns:
        None
    """
    csv_file_path = f"{dest_dir}/{filename}.csv"
    df.to_csv(csv_file_path, index=False)
    logger.info(f"Exported {filename} to {csv_file_path}")
