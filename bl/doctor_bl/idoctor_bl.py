from abc import abstractmethod
from typing import List

from bl.base_bl.ibase_bl import IBaseBl
from modals.doctor import Doctor
from modals.slot import Slot

class IDoctorBl(IBaseBl):
    @abstractmethod
    def add_doctor(self, name: str, type: str) -> None:
        pass

    @abstractmethod
    def show_doctors(self) -> None:
        pass

    @abstractmethod
    def _get_doctor(self, name: str) -> Doctor:
        pass

    @abstractmethod
    def add_service_slot(self, doctor_name: str, slot: str) -> None:
        pass

    @abstractmethod
    def _get_available_slots(self, doctor_name: str) -> List[Slot]:
        pass

    @abstractmethod
    def show_available_slots(self, doctor_name: str) -> None:
        pass

    @abstractmethod
    def add_booked_slot(self, doctor_name:str, slot: str) -> None:
        pass