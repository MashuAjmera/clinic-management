from abc import abstractmethod

from bl.base_bl.ibase_bl import IBaseBl


class IBookingBl(IBaseBl):
    @abstractmethod
    def add_booking(self, doctor_name: str, patient_name: str, slot: str) -> None:
        pass

    @abstractmethod
    def show_patient_bookings(self, name: str) -> None:
        pass

    @abstractmethod
    def show_doctor_bookings(self, name: str) -> None:
        pass