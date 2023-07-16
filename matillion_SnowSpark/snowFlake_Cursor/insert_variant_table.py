# https://community.snowflake.com/s/question/0D50Z000093RKojSAG/how-can-i-insert-json-string-to-snowflake-variant-column-using-python

import snowflake.connector
import json

# Sample JSON string
var = {
    "student": {
        "name": "John Smith",
        "age": 10
    }
}

a = [{"gtin": "062600964328", "gtin14": "00062600964328", "gln": "0068780050639", "ims": "ecommerceContent",
      "baseGln": "0062600000019", "state": "updated"},
     {"gtin": "062600964328", "gtin14": "00062600964328", "gln": "0068780050639", "ims": "marketingContent",
      "baseGln": "0062600000019", "state": "updated"},
     {"gtin": "062600964328", "gtin14": "00062600964328", "gln": "0068780050639", "ims": "planoContent",
      "baseGln": "0062600000019", "state": "brand-new"},
     {"gtin": "062600230706", "gtin14": "00062600230706", "gln": "0068780050639", "ims": "ecommerceContent",
      "baseGln": "0062600000019", "state": "updated"},
     {"gtin": "062600230706", "gtin14": "00062600230706", "gln": "0068780050639", "ims": "marketingContent",
      "baseGln": "0062600000019", "state": "updated"},
     {"gtin": "062600230706", "gtin14": "00062600230706", "gln": "0068780050639", "ims": "planoContent",
      "baseGln": "0062600000019", "state": "brand-new"},
     {"gtin": "062600964410", "gtin14": "00062600964410", "gln": "0068780050639", "ims": "ecommerceContent",
      "baseGln": "0062600000019", "state": "updated"},
     {"gtin": "062600964410", "gtin14": "00062600964410", "gln": "0068780050639", "ims": "marketingContent",
      "baseGln": "0062600000019", "state": "updated"},
     {"gtin": "062600964410", "gtin14": "00062600964410", "gln": "0068780050639", "ims": "planoContent",
      "baseGln": "0062600000019", "state": "brand-new"},
     {"gtin": "062600964960", "gtin14": "00062600964960", "gln": "0068780050639", "ims": "ecommerceContent",
      "baseGln": "0062600000019", "state": "updated"},
     {"gtin": "062600964960", "gtin14": "00062600964960", "gln": "0068780050639", "ims": "marketingContent",
      "baseGln": "0062600000019", "state": "updated"},
     {"gtin": "062600964960", "gtin14": "00062600964960", "gln": "0068780050639", "ims": "planoContent",
      "baseGln": "0062600000019", "state": "brand-new"},
     {"gtin": "062600262509", "gtin14": "00062600262509", "gln": "0068780050639", "ims": "ecommerceContent",
      "baseGln": "0062600000019", "state": "updated"},
     {"gtin": "062600262509", "gtin14": "00062600262509", "gln": "0068780050639", "ims": "marketingContent",
      "baseGln": "0062600000019", "state": "updated"},
     {"gtin": "062600262509", "gtin14": "00062600262509", "gln": "0068780050639", "ims": "planoContent",
      "baseGln": "0062600000019", "state": "brand-new"}]
b = '[{"gtin": "062600964328", "gtin14": "00062600964328", "gln": "0068780050639", "ims": "ecommerceContent", "baseGln": "0062600000019", "state": "updated"}, {"gtin": "062600964328", "gtin14": "00062600964328", "gln": "0068780050639", "ims": "marketingContent", "baseGln": "0062600000019", "state": "updated"}, {"gtin": "062600964328", "gtin14": "00062600964328", "gln": "0068780050639", "ims": "planoContent", "baseGln": "0062600000019", "state": "brand-new"}, {"gtin": "062600230706", "gtin14": "00062600230706", "gln": "0068780050639", "ims": "ecommerceContent", "baseGln": "0062600000019", "state": "updated"}, {"gtin": "062600230706", "gtin14": "00062600230706", "gln": "0068780050639", "ims": "marketingContent", "baseGln": "0062600000019", "state": "updated"}, {"gtin": "062600230706", "gtin14": "00062600230706", "gln": "0068780050639", "ims": "planoContent", "baseGln": "0062600000019", "state": "brand-new"}, {"gtin": "062600964410", "gtin14": "00062600964410", "gln": "0068780050639", "ims": "ecommerceContent", "baseGln": "0062600000019", "state": "updated"}, {"gtin": "062600964410", "gtin14": "00062600964410", "gln": "0068780050639", "ims": "marketingContent", "baseGln": "0062600000019", "state": "updated"}, {"gtin": "062600964410", "gtin14": "00062600964410", "gln": "0068780050639", "ims": "planoContent", "baseGln": "0062600000019", "state": "brand-new"}, {"gtin": "062600964960", "gtin14": "00062600964960", "gln": "0068780050639", "ims": "ecommerceContent", "baseGln": "0062600000019", "state": "updated"}, {"gtin": "062600964960", "gtin14": "00062600964960", "gln": "0068780050639", "ims": "marketingContent", "baseGln": "0062600000019", "state": "updated"}, {"gtin": "062600964960", "gtin14": "00062600964960", "gln": "0068780050639", "ims": "planoContent", "baseGln": "0062600000019", "state": "brand-new"}, {"gtin": "062600262509", "gtin14": "00062600262509", "gln": "0068780050639", "ims": "ecommerceContent", "baseGln": "0062600000019", "state": "updated"}, {"gtin": "062600262509", "gtin14": "00062600262509", "gln": "0068780050639", "ims": "marketingContent", "baseGln": "0062600000019", "state": "updated"}, {"gtin": "062600262509", "gtin14": "00062600262509", "gln": "0068780050639", "ims": "planoContent", "baseGln": "0062600000019", "state": "brand-new"}]'
import ast
b = ast.literal_eval(b)
print(b)
print(a == b)
print(json.dumps(a))
print(json.dumps(b))
print(type(a))
print(type(b))

# Connect to your Snowflake account
ctx = snowflake.connector.connect(
    account='mckesson.canada-central.azure',
    user='SSIS_INGEST_AU',
    password='Ev?PAGOnAscT',
    database='DEMO_DB',
    schema='ALF_DB_WH',
    role='DEV_ENT_DW_ENGINEER_FR',
    warehouse='DEMO_WH'

    # user = 'SSIS_INGEST_AU'
    # password = 'Ev?PAGOnAscT'
    # account = 'mckesson.canada-central.azure'
    # warehouse = 'DEMO_WH'
    # database_qualtrics = 'DEV_ENT_PL_DATALAKE_CA_DB'
    # database = 'DEMO_DB'
    # schema = 'ALF_SCHEMA'
    # schema_qualtrics = 'QUALTRICS_DATA_SRC'
    # role = 'DEV_ENT_DW_ENGINEER_FR'
)
cs = ctx.cursor()
try:
    print('a')
    cs.execute("create or replace transient table test_json_load (scr variant)")
    cs.execute("insert into test_json_load (select PARSE_JSON('%s'))" % json.dumps(a))
    # cs.execute("insert into test_json_load (select PARSE_JSON('%s'))" % json.dumps(c))
finally:
    cs.close()
ctx.close()


