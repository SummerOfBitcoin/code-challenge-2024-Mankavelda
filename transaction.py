import json

class Transaction:
    def __init__(self, txid, vin, vout):
        """
        Initialize a Transaction object with provided attributes.
        """
        self.txid = txid
        self.vin = vin
        self.vout = vout

    def is_valid(self):
        """
        Check if the transaction is valid.
        """
        if not self.txid or not self.vin or not self.vout:
            return False
        if len(self.vin) != 1 or len(self.vout) != 2:
            return False
        return True

def parse_transaction_file(file_path):
    """
    Parse a transaction file and return a Transaction object if valid.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            txid = data.get('txid')
            vin = data.get('vin')
            vout = data.get('vout')
            if txid is None or vin is None or vout is None:
                return None
            return Transaction(txid, vin, vout)
    except Exception as e:
        return None
