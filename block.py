import hashlib

class Block:
    def __init__(self, transactions, previous_hash, difficulty_target):
        """
        Initialize a Block object with provided attributes.
        """
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.difficulty_target = difficulty_target
        self.nonce = 0

    def serialize(self):
        """
        Serialize the block data.
        """
        block_data = ""
        for transaction in self.transactions:
            block_data += transaction.txid + '\n'
        return block_data

    def calculate_block_hash(self):
        """
        Calculate the hash of the block header.
        """
        header = self.serialize() + self.previous_hash + str(self.nonce)
        return hashlib.sha256(header.encode()).hexdigest()

    def mine_block(self):
        """
        Mine the block by adjusting the nonce until the hash meets the difficulty target.
        """
        while True:
            block_hash = self.calculate_block_hash()
            if int(block_hash, 16) < int(self.difficulty_target, 16):
                return self
            self.nonce += 1
