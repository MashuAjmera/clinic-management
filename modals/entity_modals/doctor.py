from dataclasses import dataclass, field

from constants.doctor_types import DoctorTypes
from modals.entity import Entity
from modals.slot import Slot

@dataclass
class Doctor(Entity):
    type: DoctorTypes = DoctorTypes.PHYSICIAN
    service_slots: set[Slot] = field(default_factory=set)
