from dataclasses import dataclass

from modals.entity_modals.doctor import Doctor
from modals.entity_modals.patient import Patient
from modals.slot import Slot

@dataclass
class Booking:
    doctor: Doctor
    patient: Patient
    slot: Slot