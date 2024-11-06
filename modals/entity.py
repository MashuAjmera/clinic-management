from dataclasses import dataclass, field

from modals.slot import Slot

@dataclass
class Entity:
    name: str
    booked_slots: set[Slot] = field(default_factory=set)