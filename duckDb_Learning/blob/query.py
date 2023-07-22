import duckdb
import adlfs, os
from dotenv import load_dotenv

load_dotenv()
AZURE_STORAGE_ACCOUNT_NAME = os.getenv('AZURE_STORAGE_ACCOUNT_NAME')
AZURE_STORAGE_ACCOUNT_KEY = os.getenv('AZURE_STORAGE_ACCOUNT_KEY')
table_path = os.getenv('table_path')
fs = adlfs.AzureBlobFileSystem(account_name=AZURE_STORAGE_ACCOUNT_NAME, account_key=AZURE_STORAGE_ACCOUNT_KEY)
# print(AZURE_STORAGE_ACCOUNT_KEY)
con = duckdb.connect()
duckdb.connect()
con.register_filesystem(fs)
# print(f" select *  from '{table_path}org.GS1CA/api=coverage/date=2023-07-19/gtin_list_0_0_0.json'")
# duckdb.sql(
#     'SELECT * FROM read_parquet("azure://samtentcadl.blob.core.windows.net/dev-dl/userdata1.parquet")').show()
# con.sql(f"-- select *  from 'azure://samtentcadl.blob.core.windows.net/dev-dl/org.GS1CA/api=coverage/date=2023-07-19/gtin_list_0_0_0.json'").show()

df = con.execute(f'''
    select *  from read_csv('{table_path}/training_azure_flights_2016.CSV')
    '''
).df()
# con.unregister_filesystem('abfs')
# df
