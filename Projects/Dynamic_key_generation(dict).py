# Problem Statement: Write a program that generates a unique key for each item in the list of items. The unique key should be generated based on the item's name and price. The key should be a SHA-1 hash of the concatenation of the item's name only. 

items = [['Laptop', 800], ['Mouse', 40], ['Keyboard', 60], ['Tablet', 200]]

import uuid
newdict = {}
for item in items:
    uid = uuid.uuid5(uuid.NAMESPACE_OID, item[0])
    key = uid.hex[:8] # -> 'uid' is an object of <class 'uuid.UUID'> but 'uid.hex' is a string representation of the UUID in hexadecimal format, hence can be sliced to get the first 8 characters of the UUID. 
    newdict[key] = item

print(newdict)
