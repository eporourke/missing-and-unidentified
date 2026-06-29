from dotenv import load_dotenv
import os
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
from datetime import date, datetime, timezone
import re

# db connection variables

load_dotenv()

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

# data variables
source_file = "2026_06_20_map_murdered.csv"
data_source = "map"
dl_date = date(2026, 6, 20)
csv_path = Path("raw/murder_accountability_project/") / source_file

df = pd.read_csv(csv_path)

# Adding variables and timestamp as columns to df before loading
df["source_file"] = source_file
df["data_source"] = data_source
df["dl_date"] = dl_date
df["load_ts"] = datetime.now(timezone.utc)

# connect to database
engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

# fix unfriendly-to-data column names
df.columns = [re.sub(r"_+", "_",
           re.sub(r"[^a-z0-9]", "_", col.strip().lower())
          ).strip("_")
    for col in df.columns]

# load into table - append if data already exists
df.to_sql(
    name="murder_accountability",
    con=engine,
    schema="raw",
#    if_exists="replace",
    if_exists="append",
    index=False,
)

print(f"Loaded {len(df)} rows into ")