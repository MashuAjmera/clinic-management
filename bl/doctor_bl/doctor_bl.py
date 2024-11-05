from typing import List
from modals.doctor import Doctor
from bl.base_bl.base_bl import BaseBl
from modals.slot import Slot

class DoctorBl(BaseBl):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DoctorBl, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.doctor_list = []
    
    def add_doctor(self, name: str, type: str) -> None:
        self.doctor_list.append(Doctor(name, type))
        print(f'Welcome Dr. {name}!')

    def show_doctors(self) -> None:
        print('Our doctors are:', end=' ')
        for doctor in self.doctor_list:
            print(f'Dr. {doctor.name} ({doctor.type})', end=', ')
        print()

    def _get_doctor(self, name) -> Doctor:
        for doctor in self.doctor_list:
            if doctor.name == name:
                return doctor
        return None

    def add_service_slot(self, doctor_name: str, slot: str) -> None:
        try:
            doctor = self._get_doctor(doctor_name)
            if not doctor:
                raise Exception(f'Dr. {doctor_name} is not registered.')
            if Slot(slot) in doctor.service_slots:
                raise Exception(f'Slot {slot} already present for Dr. {doctor_name}')
            doctor.service_slots.add(Slot(slot))
            print(f'{slot} slot added successfully for Dr. {doctor_name}')
        except Exception as e:
            print(e)

    def _get_available_slots(self, doctor_name) -> List[Slot]:
        try:
            doctor = self._get_doctor(doctor_name)
            if not doctor:
                raise Exception(f'Dr. {doctor_name} is not registered.')
            return doctor.service_slots - doctor.booked_slots
        except Exception as e:
            print(e)

    def show_available_slots(self, doctor_name: str) -> None:
        available_slots = self._get_available_slots(doctor_name)
        print(f'Available slots for Dr. {doctor_name} are: {[slot.time for slot in available_slots]}.')

    def add_booked_slot(self, doctor_name: str, slot: Slot) -> None:
        try:
            if slot not in self._get_available_slots(doctor_name):
                raise Exception(f'Dr. {doctor_name} not available at {slot.time}.')
            doctor = self._get_doctor(doctor_name)
            doctor.booked_slots.add(slot)
        except Exception as e:
            raise