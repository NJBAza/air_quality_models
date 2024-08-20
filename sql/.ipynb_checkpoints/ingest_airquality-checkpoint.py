import argparse
import os
import zipfile
from io import BytesIO

import pandas as pd
import requests
from sqlalchemy import create_engine


def download_and_extract_csv(url):
    """Download and extract the CSV file from a ZIP archive if necessary."""
    if url.endswith(".zip"):
        response = requests.get(url)
        if response.status_code == 200:
            with zipfile.ZipFile(BytesIO(response.content)) as z:
                # Extract the first CSV file found
                for file_name in z.namelist():
                    if file_name.endswith(".csv"):
                        with z.open(file_name) as csv_file:
                            return pd.read_csv(csv_file, delimiter=";", engine="python")
        else:
            raise Exception(
                f"Failed to download the file from {url}. Status code: {response.status_code}"
            )
    else:
        return pd.read_csv(url, delimiter=";", engine="python")


def process_and_ingest_data(df, table_name, engine):
    """Process the DataFrame and ingest it into the PostgreSQL database."""
    # Drop columns and rows where all elements are NaN
    df = df.dropna(how="all", axis=1).dropna(how="all", axis=0)

    # Convert date and time columns
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y", errors="coerce")
    df["Time"] = pd.to_datetime(
        df["Time"].str.replace(".", ":"), format="%H:%M:%S", errors="coerce"
    ).dt.time

    # Convert other columns to float
    for col in ["CO(GT)", "C6H6(GT)", "T", "RH", "AH"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col].str.replace(",", "."), errors="coerce")

    # Write the DataFrame to PostgreSQL
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists="replace")  # Create table
    df.to_sql(name=table_name, con=engine, if_exists="append", index=False)  # Insert data


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    table_name = params.table_name
    db = params.db
    url = params.url

    # Download and process the CSV file
    df = download_and_extract_csv(url)

    # Connect to PostgreSQL
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    # Process the DataFrame and ingest it into the database
    process_and_ingest_data(df, table_name, engine)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingesting airquality data to PostgreSQL")

    parser.add_argument("--user", help="user name for PostgreSQL", required=True)
    parser.add_argument("--password", help="password for PostgreSQL", required=True)
    parser.add_argument("--host", help="host for PostgreSQL", required=True)
    parser.add_argument("--port", help="port for PostgreSQL", required=True)
    parser.add_argument("--db", help="database name for PostgreSQL", required=True)
    parser.add_argument("--table_name", help="table name for PostgreSQL", required=True)
    parser.add_argument(
        "--url", help="URL of the CSV file or ZIP file containing the CSV", required=True
    )

    args = parser.parse_args()
    main(args)


date_features_train = pd.DataFrame(
    {
        "day": df["Date"].dt.day,
        "year": df["Date"].dt.year,
        "quarter": df["Date"].dt.quarter,
        "month": df["Date"].dt.month,
        "weekday": df["Date"].dt.dayofweek,
        "week_year": df["Date"].dt.isocalendar().week,
    }
)
