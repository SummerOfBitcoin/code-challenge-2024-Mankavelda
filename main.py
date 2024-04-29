import os
from transaction import parse_transaction_file
from block import Block
from mining import mine_block

def load_transactions_from_mempool():
    """
    Load valid transactions from the mempool directory.
    """
    transactions = []
    mempool_dir = "mempool"
    for filename in os.listdir(mempool_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(mempool_dir, filename)
            transaction = parse_transaction_file(file_path)
            if transaction is not None and transaction.is_valid():
                transactions.append(transaction)
    return transactions

def main():
    # Load transactions from mempool
    transactions = load_transactions_from_mempool()

    if not transactions:
        print("No valid transactions found in mempool.")
        return

    # Create genesis block
    genesis_block = Block(transactions, "0", "0000ffff00000000000000000000000000000000000000000000000000000000")

    # Mine the block
    mined_block = mine_block(genesis_block, genesis_block.difficulty_target)

    # Output results to output.txt
    with open("output.txt", "w") as f:
        f.write(f"Block Header: {mined_block.calculate_block_hash()}\n")
        f.write(f"Serialized Coinbase Transaction: {mined_block.serialize()}\n")
        f.write("Transaction IDs (txids) of mined transactions:\n")
        for transaction in transactions:
            f.write(f"{transaction.txid}\n")

if __name__ == "__main__":
    main()
