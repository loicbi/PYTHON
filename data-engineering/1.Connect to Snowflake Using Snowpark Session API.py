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
# print connection params
print("The Parameter :", connection_param)

# creating a session object
session = Session.builder.configs(connection_param).create()

# print values from session object to test
print("\n\t Current Account Name: ", session.get_current_account())
print("\t Current Database Name: ", session.get_current_database())
print("\t Current Schema Name: ", session.get_current_schema())
print("\t Current Role Name: ", session.get_current_role())
print("\t Current Warehouse Name: ", session.get_current_warehouse())
print("\t Fully Qualified Schema Name: ", session.get_fully_qualified_current_schema(), "\n")

print("Session Object Type:", type(session))
# closing the session
session.close()


