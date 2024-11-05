from dataclasses import dataclass

@dataclass
class Doctor:
    name: str
    type: str
    service_slots = set()
    booked_slots = set()
