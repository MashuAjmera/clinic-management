from dataclasses import dataclass

@dataclass
class Slot:
    time: str

    def __eq__(self, other):
        return isinstance(other, Slot) and self.time == other.time

    def __hash__(self):
        # Hash based on name and specialty, ensuring consistent hashing
        return hash(self.time)