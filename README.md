# Spotify Personal Listening Analytics

Automated ETL pipeline that extracts personal Spotify listening data via API, stores it in PostgreSQL and visualizes trends in Power BI.

## Stack
- Python (spotipy, pandas, sqlalchemy)
- PostgreSQL
- Power BI

## Features
- Extracts top 50 tracks across 3 time periods (short / medium / long term)
- Longitudinal analysis of personal listening habits over time

## Pipeline
```
Spotify API → Python (extract.py) → Pandas → PostgreSQL → Power BI
```

## How to run
1. Clone repo
2. Create `.env` with your Spotify API credentials
3. Run `python extract.py`
4. Run `python load.py`