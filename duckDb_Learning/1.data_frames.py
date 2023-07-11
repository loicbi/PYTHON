import duckdb, time
import os

# pandas
start_time_pd = time.time()
import pandas as pd

pandas_df = pd.DataFrame({'tel': [4812524585]})
print(f"{pandas_df}")
duckdb.sql('SELECT * FROM pandas_df;').show()
end_time_pd = time.time() - start_time_pd
duckdb.sql(f'SELECT {end_time_pd} as timeExecuted').show()

# polars
start_time_pl = time.time()
import polars as pl

polars_df = pl.DataFrame({'age': [30]})
duckdb.sql('SELECT * FROM polars_df').show()
end_time_pl = time.time() - start_time_pl
duckdb.sql(f'SELECT {end_time_pl} as timeExecuted').show()

# Result Conversation
(duckdb.sql('SELECT 10').fetchall())  # Python Object
(duckdb.sql('SELECT 10').df())  # Pandas Dataframe
(duckdb.sql('SELECT 10').pl())  # Polars Dataframe
(duckdb.sql('SELECT 10').arrow())  # Arrow Table
(duckdb.sql('SELECT 10').fetchnumpy())  # NumPy Array

# Writing Data top Disk
duckdb.sql("SELECT 'Loic' as colVarchar, 123 as NumberCol").write_parquet(
    'C:/Users/aseka/source/_________LOIC_BI__________/_______Learning__All/SnowFlake/PYTHON/datasets/output/out.parquet',
    compression='gzip')

# Copy to file
duckdb.sql(
    "COPY (SELECT 'Loic Andre' as colVarchar, 12345 as NumberCol) TO 'C:/Users/aseka/source/_________LOIC_BI__________/_______Learning__All/SnowFlake/python/datasets/output/out.parquet'")

# Copy file csv to parquet
duckdb.sql(
    'SELECT * FROM "C:/Users/aseka/source/_________LOIC_BI__________/_______Learning__All/SnowFlake/python/datasets/training_azure_flights_2016.csv"').write_parquet(
    'C:/Users/aseka/source/_________LOIC_BI__________/_______Learning__All/SnowFlake/PYTHON/datasets/output/training_azure_flights_2016.parquet')

# Persistent Storage
con = duckdb.connect('connection/file.db')
con.sql("CREATE OR REPLACE TABLE t1 AS SELECT * FROM read_csv_auto('C:/Users/aseka/source/_________LOIC_BI__________/_______Learning__All/SnowFlake/python/datasets/training_azure_flights_2016.csv');")
# con.sql('INSERT INTO  test(i) VALUES (87878)')
(con.table('test'))
# con.sql('select * from test').show()
# con.sql('select * from t1').show()
con.close()
