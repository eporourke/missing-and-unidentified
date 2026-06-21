from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

source_file = "2026_06_19_missing_male_white_before_2026.csv"

csv_path = Path("raw/namus/") / source_file

df = pd.read_csv(csv_path)

# Add provenance column BEFORE loading
df["source_file"] = source_file

engine = create_engine(
    "postgresql+psycopg2://postgres:PASSWORDHERE@localhost:5433/missing-unidentified-persons"
)

df.to_sql(
    name="namus_missing",
    con=engine,
    schema="raw",
#    if_exists="replace",
    if_exists="append",
    index=False,
)

print(f"Loaded {len(df)} rows into that database name you put up there")