
from fastapi import FastAPI
from .blockchain import Blockchain
from .simulator import simulate_supply_chain

app = FastAPI()
blockchain = Blockchain()

@app.get("/simulate-once")
def simulate_once():
    events = simulate_supply_chain()
    blocks = []
    for event in events:
        block = blockchain.add_block(event)
        blocks.append({
            "index": block.index,
            "timestamp": block.timestamp.isoformat(),
            "event_type": block.event.event_type,
            "previous_hash": block.previous_hash,
            "hash": block.hash,
        })
    return {
        "valid_chain": blockchain.is_valid(),
        "blocks": blocks,
    }
