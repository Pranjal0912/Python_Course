import uuid
# UUID (Universally Unique Identifier) is a 128-bit number used to uniquely identify information in computer systems. The uuid module in Python provides functions to generate UUIDs.

# -> How a UUID is generated:
#  - It uses a combination of the current time, the machine's network address (MAC address), and random numbers to create a unique identifier.

# Function of uuid module:

# 1. uuid.uuid1(): Generates a UUID based on the host ID and current time.

uid = uuid.uuid1()
print("UUID1:", uid, "| Integer representation:", uid.int) #-> This function generates a UUID based on the host ID and current time. It uses the MAC address of the computer and the current timestamp to create a unique identifier.

# 2. uuid.uuid3(): Generates a UUID based on the MD5 hash of a namespace identifier and a name. (MD5 is a widely used cryptographic hash function that produces a 128-bit hash value. It is commonly used to verify data integrity.)
# Few examples of namespace identifiers are:

# - uuid.NAMESPACE_DNS: For domain names.
uid = uuid.uuid3(uuid.NAMESPACE_DNS, 'example.com')
print("UUID3:", uid, "| Integer representation:", uid.int) 

# - uuid.NAMESPACE_URL: For URLs.
uid2 = uuid.uuid3(uuid.NAMESPACE_URL, 'https://www.example.com')
print("UUID3:", uid2, "| Integer representation:", uid2.int) 
print(uid2)#-> It is deterministic, meaning that the same namespace and name will always produce the same UUID.

# - uuid.NAMESPACE_OID: For ISO OIDs.
uid3 = uuid.uuid3(uuid.NAMESPACE_OID, 'CPU')
print("UUID3:", uid3, "| Integer representation:", uid3.int)

# - uuid.NAMESPACE_X500: For X.500 distinguished names.
uid4 = uuid.uuid3(uuid.NAMESPACE_X500, 'CN=John Doe, OU=Sales, O=Example Corp, C=US')
print("UUID3:", uid4, "| Integer representation:", uid4.int)

# 3. uuid.uuid4(): Generates a random UUID.
uid = uuid.uuid4()
print("UUID4:", uid, "| Integer representation:", uid.int) #-> This function generates a random UUID. It uses random numbers to create a unique identifier.

# 4. uuid.uuid5(): Generates a UUID based on the SHA-1 hash of a namespace identifier and a name. (SHA-1 is a cryptographic hash function that produces a 160-bit hash value. It is commonly used for data integrity verification and digital signatures.)
# The usage of uuid5() is similar to uuid3(), but it uses the SHA-1 hashing algorithm instead of MD5. It is also deterministic, meaning that the same namespace and name will always produce the same UUID.
uid = uuid.uuid5(uuid.NAMESPACE_DNS, 'example.com')
print("UUID5:", uid, "| Integer representation:", uid.int)

