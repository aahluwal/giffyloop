import random


HASH_LENGTH = 4
HASH_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def hash_url(url):
    hash_key = []
    for i in range(0, HASH_LENGTH):
	hash_key.append(random.choice(HASH_CHARS))
    return ''.join(hash_key)
