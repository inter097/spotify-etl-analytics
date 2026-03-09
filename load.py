import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv("DB_PASSWORD")
engine = create_engine(f"postgresql://postgres:{password}@localhost:5432/spotify_etl")

df = pd.read_csv("spotify_raw.csv")

df.to_sql("canciones", engine, if_exists="append", index=False)

print(f"✅ {len(df)} registros insertados en PostgreSQL!")