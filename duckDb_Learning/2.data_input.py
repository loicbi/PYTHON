import duckdb

r1 = duckdb.sql('SELECT 42 AS i, 585.33 as Number ')
print(f"r1 is: /n{r1}")
(duckdb.sql('SELECT i * 2 AS k, Number FROM r1').show())
''' ---  OR --- '''
# print(duckdb.execute('SELECT i * 2 AS k, Number FROM r1').df())

# Data Input
# duckdb.read_csv(
#     'C:/Users/aseka/source/_________LOIC_BI__________/_______Learning__All/SnowFlake/python/datasets/training_azure_flights_2016.CSV').show()
duckdb.sql(
    'SELECT * FROM "C:/Users/aseka/source/_________LOIC_BI__________/_______Learning__All/SnowFlake/python/datasets/training_azure_flights_2016.csv" limit 1').show()

# set read_csv inside

# duckdb.read_csv(
#     "//datasets/training_azure_flights_2016.CSV",
#     header=True, delimiter=',',
# ).show()

# Parquet
duckdb.sql(
    'SELECT * FROM "C:/Users/aseka/source/_________LOIC_BI__________/_______Learning__All/SnowFlake/python/datasets/userdata1.parquet"').show()

# JSON
duckdb.sql(
    'SELECT * FROM "C:/Users/aseka/source/_________LOIC_BI__________/_______Learning__All/SnowFlake/python/datasets/example.json"').show()
