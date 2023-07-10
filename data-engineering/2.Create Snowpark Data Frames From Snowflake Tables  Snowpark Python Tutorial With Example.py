# import snowflake snowpark library
from snowflake.snowpark import Session

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
# approach-1
# call table function on session API to get dataframe
# Spark Version => spark.table() or spark.read.table()
emp_phones_df = session.table("EMP_PHONES")

print(type(emp_phones_df))
# display data
emp_phones_df.show(2)


# # approach-2
database = "DEMO_DB"
schema = "ALF_SCHEMA"
emp_df = session.table([database,schema,"EMPLOYEE_JSON"])

# display data
emp_df.show(2)
#
# print data type
print(type(emp_df))

# closing the session
session.close()
