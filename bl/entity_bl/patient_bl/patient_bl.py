from bl.entity_bl.entity_bl import EntityBl
from bl.entity_bl.patient_bl.ipatient_bl import IPatientBl
from bl.entity_bl.patient_bl.ipatient_bl import IPatientBl
from modals.entity_modals.patient import Patient
from modals.slot import Slot
from utilities.singleton import Singleton

class PatientBl(EntityBl, IPatientBl, Singleton):

    def _check_availability(self, entity: Patient, slot: Slot):
        if slot in entity.booked_slots:
            raise Exception(f'Patient {entity.name} already booked for {slot.time} slot.')