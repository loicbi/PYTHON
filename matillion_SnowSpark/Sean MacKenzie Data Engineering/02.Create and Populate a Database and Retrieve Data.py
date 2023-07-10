# https://youtu.be/yvdwKpm1P7A?list=PLnfNzgd6iu9Xg0DVJyAweipk15MHSFfMP
import snowflake.connector
import config

connection_to_snowflake = snowflake.connector.connect(
    user=config.user,
    password=config.password,
    account=config.account,
    warehouse=config.warehouse

)

cs = connection_to_snowflake.cursor()

try:
    cs.execute('SELECT CURRENT_VERSION()')
    row = cs.fetchone()
    print(row[0])
    # create schema
    sql = "USE DEMO_DB;"
    print("Using dataBase ")
    cs.execute(sql)
    print("Creating schema")
    sql = "CREATE SCHEMA IF NOT EXISTS ALF_SNOWPARK;"
    cs.execute(sql)
    print("Complete")
    cs.execute('SELECT CURRENT_WAREHOUSE()')
    row = cs.fetchone()
    print(row[0])
    print("Creating table")
    sql = "CREATE OR REPLACE TABLE snowpark"
finally:
    cs.close()
connection_to_snowflake.close()

