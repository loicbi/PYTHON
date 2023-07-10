# import snowflake snowpark library
from snowflake.snowpark import Session
# from snowflake.snowpark.types import StructType, StructField, StringType

print("\n\tSnowpark Program Starting...")
# define connection parameter dictionary with role,database & schema


connection_param = {
    "ACCOUNT": "mckesson.canada-central.azure",
    "USER": "SSIS_INGEST_AU",
    "PASSWORD": "Ev?PAGOnAscT",
    "warehouse": 'DEMO_WH',
    "database": 'DEMO_DB',
    "schema": 'ALF_SCHEMA',
    "ROLE": "DEV_ENT_DW_ENGINEER_FR",
}
# creating a session object
session = Session.builder.configs(connection_param).create()


