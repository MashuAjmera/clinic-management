from bl.base_bl.base_bl import BaseBl
from bl.patient_bl.ipatient_bl import IPatientBl
from modals.patient import Patient

class PatientBl(BaseBl, IPatientBl):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PatientBl, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.patients = []
    
    def add_patient(self, name: str) -> None:
        try:
            if self._get_patient(name):
                raise Exception(f'Patient {name} already exists')
            self.patients.append(Patient(name))
            print(f'Welcome patient {name}!')
        except Exception as e:
            print(e)
    
    def _get_patient(self, name: str) -> Patient:
        for patient in self.patients:
            if patient.name == name:
                return patient
        return None