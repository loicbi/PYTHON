import duckdb
import os

'''CSV Files'''
path = '//datasets/'
# read from a file using fully auto-detected settings
duckdb.read_csv(f'{path}training_azure_flights_2016.CSV')
# read multiple CSV files from a folder
# duckdb.read_csv('C:/Users/aseka/source/_________LOIC_BI__________/_______Learning__All/SnowFlake/python/datasets/*.CSV')
# specify options on how the CSV is formatted internally
print(duckdb.read_csv(f'{path}training_azure_flights_2016.CSV', header=True, sep=','))
# override types of the first two columns
duckdb.read_csv(f'{path}training_azure_flights_2016.CSV', dtype=['int', 'varchar'])

# use the (experimental) parallel CSV reader
duckdb.read_csv(f'{path}training_azure_flights_2016.CSV', parallel=True).show()
# # directly read a CSV file from within SQL
# print(duckdb.sql(f"SELECT * FROM '{path}training_azure_flights_2016.CSV'").fetchall())


"""DataFrames & Arrow Tables"""
import pandas as pd

con = duckdb.connect('connection/file.db')

my_dictionary = {}
my_dictionary['test_df'] = pd.DataFrame.from_dict({"i": [1, 2, 3, 4], "j": ["one", "two", "three", "four"]})
duckdb.register('test_df_view', my_dictionary['test_df'])
duckdb.sql('SELECT * FROM test_df_view').fetchall()
duckdb.sql(f"COPY (SELECT * FROM test_df_view) TO '{path}output/test_df.parquet'")

# create a new table from the contents of a DataFrame
con.register('test_df_view', my_dictionary['test_df'])
con.sql('SELECT * FROM test_df_view').show()
con.execute(f"CREATE OR REPLACE TABLE test_df_table AS SELECT * FROM test_df_view")
print(con.table('test_df_table'))
# insert into an existing table from the contents of a DataFrame
con.sql('SELECT * FROM test_df_table').show()

con.close()
