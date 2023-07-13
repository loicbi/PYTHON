import duckdb
from adlfs import AzureBlobFileSystem
import pyarrow.parquet as pq
import pyarrow.dataset as ds



account_name = "xxxxx"
account_key = "xxxxx"
abfs = AzureBlobFileSystem( account_name = account_name, account_key = account_key, container_name = "data")
pqdata = ds.dataset("path/inside/abfs", filesystem=abfs)


conn = duckdb.connect(":memory:")
conn.execute("SELECT * from pqdata LIMIT 10")


