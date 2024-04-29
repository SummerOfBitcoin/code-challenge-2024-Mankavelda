import hashlib

def calculate_hash(data):
    """
    Calculate the hash of the given data.
    """
    return hashlib.sha256(data.encode()).hexdigest()

def mine_block(block, difficulty_target):
    """
    Mine the block by adjusting the nonce until the hash meets the difficulty target.
    """
    while True:
        block.nonce += 1
        block_hash = int(calculate_hash(block.serialize()), 16)
        if block_hash < int(difficulty_target, 16):
            return block
