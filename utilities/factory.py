from bl.booking_bl.ibooking_bl import IBookingBl
from bl.entity_bl.doctor_bl.idoctor_bl import IDoctorBl
from bl.entity_bl.patient_bl.ipatient_bl import IPatientBl


class Factory:
    @staticmethod
    def get_doctor_bl() -> IDoctorBl:
        from bl.entity_bl.doctor_bl.doctor_bl import DoctorBl
        return DoctorBl()

    @staticmethod
    def get_patient_bl() -> IPatientBl:
        from bl.entity_bl.patient_bl.patient_bl import PatientBl
        return PatientBl()

    @staticmethod
    def get_booking_bl() -> IBookingBl:
        from bl.booking_bl.booking_bl import BookingBl
        return BookingBl()