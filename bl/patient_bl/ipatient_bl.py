from abc import ABC, abstractmethod
from bl.base_bl.ibase_bl import IBaseBl
from modals.patient import Patient

class IPatientBl(IBaseBl):
    @abstractmethod
    def add_patient(self, name) -> None:
        pass

    @abstractmethod
    def _get_patient(self, name) -> Patient:
        pass