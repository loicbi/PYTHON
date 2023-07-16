import duckdb
import adlfs, os
from dotenv import load_dotenv

load_dotenv()
AZURE_STORAGE_ACCOUNT_NAME = os.getenv('AZURE_STORAGE_ACCOUNT_NAME')
AZURE_STORAGE_ACCOUNT_KEY = os.getenv('AZURE_STORAGE_ACCOUNT_KEY')
table_path = os.getenv('table_path')
fs = adlfs.AzureBlobFileSystem(account_name=AZURE_STORAGE_ACCOUNT_NAME, account_key=AZURE_STORAGE_ACCOUNT_KEY)
print(fs.url('azure://dev-dl/ca/THIRD_PARTY_DATA/GS1/coverage/ecommerceContent_GTIN_LIST.json_0_0_0.json'))
con = duckdb.connect()
con.register_filesystem(fs)
df = con.sql(f'''
    select *
    from 'https://samtdaentcadl.blob.core.windows.net/azure//dev-dl/ca/THIRD_PARTY_DATA/GS1/coverage/ecommerceContent_GTIN_LIST.json_0_0_0.json?se=2023-07-13T05%3A52%3A34Z&sp=r&sv=2023-01-03&sr=b&sig=cCDV8v1cGtTjTrypdXLsq6pifINTmWjgqRQ5PUNmMZc%3D'
    limit 10
    '''
             ).show()
# con.unregister_filesystem('abfs')
# df
