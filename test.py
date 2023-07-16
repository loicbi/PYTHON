import json

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

print(len(a))
# for i in range(len(a)):
#     print(a[i]['gtin'])
a = json.dumps(a)

print(a)
