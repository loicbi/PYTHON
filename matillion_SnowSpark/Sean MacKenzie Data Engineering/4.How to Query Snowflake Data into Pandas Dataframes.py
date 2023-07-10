# https://youtu.be/fGtSH1QEeE4?list=PLnfNzgd6iu9Xg0DVJyAweipk15MHSFfMP
import config
from snowflake.snowpark import Session
import pandas as pd

connection_param = {
    "ACCOUNT": "mckesson.canada-central.azure",
    "USER": "SSIS_INGEST_AU",
    "PASSWORD": "Ev?PAGOnAscT",
    "warehouse": 'DEMO_WH',
    "database": 'DEMO_DB',
    "schema": 'ALF_SCHEMA',
    "ROLE": "DEV_ENT_DW_ENGINEER_FR",
}
#Invoking Snowpark Session for Establishing Connection
session = Session.builder.configs(connection_param).create()
try:
    query_1  = session.sql("SELECT VALUES_SFPHONE FROM DEV_ENT_DL_CA_DB.QUALTRICS_DATA_SRC.PIVOT_SV_2MMFEB1OKLN3F9I")
    query_2  = session.sql("SELECT VALUES_SFPHONE FROM DEV_ENT_DL_CA_DB.QUALTRICS_DATA_SRC.PIVOT_SV_2MMFEB1OKLN3F9I").collect()
    # query_1.show()
    # print(query_2)

    df = session.table('"DEV_ENT_DL_CA_DB"."QUALTRICS_DATA_SRC"."PIVOT_SV_2MMFEB1OKLN3F9I"')

    for row in df.to_local_iterator():
        if row.RESPONSEID == 'R_yr6xvClmqs9fwNb':
            print(row.VALUES_SFPHONE)
            query = session.sql("UPDATE DEV_ENT_DL_CA_DB.QUALTRICS_DATA_SRC.PIVOT_SV_2MMFEB1OKLN3F9I  SET VALUES_SFPHONE = '9999' WHERE RESPONSEID = 'R_yr6xvClmqs9fwNb'").collect()
            #query.show()

finally:
    session.close()
