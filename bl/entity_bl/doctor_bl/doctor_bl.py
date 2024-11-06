from typing import List
from bl.entity_bl.doctor_bl.idoctor_bl import IDoctorBl
from bl.entity_bl.entity_bl import EntityBl
from constants.doctor_types import DoctorTypes
from modals.entity_modals.doctor import Doctor
from modals.slot import Slot
from utilities.singleton import Singleton

class DoctorBl(EntityBl, IDoctorBl, Singleton):

    def add(self, name: str, type: DoctorTypes) -> None:
        super().add(name, Doctor)
        self.entities[-1].type = type

    def _check_availability(self, entity: Doctor, slot: Slot):
        if slot not in self._get_available_slots(entity):
            raise Exception(f'Patient {entity.name} already booked for {slot.time} slot.')

    def show_doctors(self) -> None:
        print('Our doctors are:', end=' ')
        for doctor in self.entities:
            print(f'Dr. {doctor.name} ({doctor.type.value})', end=', ')
        print()

    def add_service_slot(self, doctor_name: str, slot: str) -> None:
        try:
            doctor = self.get(doctor_name)
            if not doctor:
                raise Exception(f'Dr. {doctor_name} is not registered.')
            if Slot(slot) in doctor.service_slots:
                raise Exception(f'Slot {slot} already present for Dr. {doctor_name}')
            doctor.service_slots.add(Slot(slot))
            print(f'{slot} slot added successfully for Dr. {doctor_name}')
        except Exception as e:
            print(e)

    def _get_available_slots(self, doctor: Doctor) -> List[Slot]:
        try:
            return doctor.service_slots - doctor.booked_slots
        except Exception as e:
            raise

    def show_available_slots(self, doctor_name: str) -> None:
        doctor = self.get(doctor_name)
        if not doctor:
            raise Exception(f'Dr. {doctor_name} is not registered.')
        available_slots = self._get_available_slots(doctor)
        print(f'Available slots for Dr. {doctor_name} are: {[slot.time for slot in available_slots]}.')

    def show_available_slots_by_type(self, doctor_type: DoctorTypes) -> List[Slot]:
        try:
            res = {}
            for doctor in self.entities:
                if doctor.type == doctor_type:
                    res[doctor.name] = [slot.time for slot in self._get_available_slots(doctor)]
            print(f'Available slots for {doctor_type.value}s are: {res}') 
        except Exception as e:
            print(e)