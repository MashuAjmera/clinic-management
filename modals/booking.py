from dataclasses import dataclass

from modals.doctor import Doctor
from modals.patient import Patient
from modals.slot import Slot

@dataclass
class Booking:
    doctor: Doctor
    patient: Patient
    slot: Slot