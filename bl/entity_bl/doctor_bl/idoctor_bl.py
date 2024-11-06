from abc import abstractmethod
from typing import List

from bl.entity_bl.entity_bl import IEntityBl
from constants.doctor_types import DoctorTypes
from modals.entity_modals.doctor import Doctor
from modals.slot import Slot

class IDoctorBl(IEntityBl):
    @abstractmethod
    def show_doctors(self) -> None:
        pass

    @abstractmethod
    def add_service_slot(self, doctor_name: str, slot: str) -> None:
        pass

    @abstractmethod
    def _get_available_slots(self, doctor: Doctor) -> List[Slot]:
        pass

    @abstractmethod
    def show_available_slots(self, doctor_name: str) -> None:
        pass

    @abstractmethod
    def show_available_slots_by_type(self, doctor_type: DoctorTypes) -> None:
        pass