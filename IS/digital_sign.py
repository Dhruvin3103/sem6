import hashlib
from rsa import rsa


def hash_message(message, algorithm):
    hasher = hashlib.new(algorithm)
    hasher.update(message.encode())
    
    return hasher.hexdigest()


message = "HelloThere!!"
hashed_message_md5 = hash_message(message, "md5")
print("MD5 hash:", hashed_message_md5)
decimal_number = int(hashed_message_md5, 16)
print(decimal_number)

# dig_sign = rsa(
#     104729,
#     104723,
#     65537,
# )
