# Block, Event dataclasses

from dataclasses import dataclass
from typing import Dict, Any
from datetime import datetime

@dataclass
class SupplyChainEvent:
    event_id: str
    event_type: str
    timestamp: datetime
    location: Dict[str, float]
    metadata: Dict[str, Any]

@dataclass
class Block:
    index: int
    timestamp: datetime
    event: SupplyChainEvent
    previous_hash: str
    hash: str
    nonce: int = 0
