# https://youtu.be/yvdwKpm1P7A?list=PLnfNzgd6iu9Xg0DVJyAweipk15MHSFfMP
import snowflake.connector

connection_to_snowflake = snowflake.connector.connect(
    user='SSIS_INGEST_AU',
    password='Ev?PAGOnAscT',
    account='mckesson.canada-central.azure',
    warehouse='DEMO_WH'

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
    print("Complete")
finally:
    cs.close()
connection_to_snowflake.close()

