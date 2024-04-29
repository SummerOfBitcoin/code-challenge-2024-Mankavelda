import random
import string
import hashlib

def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def generate_nonce():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
