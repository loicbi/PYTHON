a = '[ {    "baseGln": "0062600000019",    "gln": "0068780050639",    "gtin": "062600246165",    "gtin14": "00062600246165",    "ims": "ecommerceContent",    "state": "updated"  },  {    "baseGln": "0062600000019",    "gln": "0068780050639",    "gtin": "062600338990",    "gtin14": "00062600338990",    "ims": "ecommerceContent",    "state": "updated"  }]'


import json
a = json.loads(a)
print(len(a))

