import duckdb

# gs1
duckdb.sql(
    'SELECT DATA_STATE_GTIN.baseGln,DATA_STATE_GTIN.gtin, DATA_STATE_GTIN.gln, DATA_STATE_GTIN.ims , DATA_STATE_GTIN.state  FROM "C:/Users/aseka/source/_________LOIC_BI__________/_______Learning__All/SnowFlake/python/datasets/example2.json"').show()

duckdb.sql(
    'SELECT DISTINCT DATA_STATE_GTIN.IMS  FROM "C:/Users/aseka/source/_________LOIC_BI__________/_______Learning__All/SnowFlake/python/datasets/example2.json"').show()



