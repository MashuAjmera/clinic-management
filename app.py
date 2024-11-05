from utilities.factory import Factory
from constants.doctor_types import DoctorTypes

doctor_bl = Factory.get_doctor_bl()
patient_bl = Factory.get_patient_bl()
booking_bl = Factory.get_booking_bl()

doctor_bl.add_doctor('Mashu', DoctorTypes.PULMONOLOGIST)
doctor_bl.add_doctor('Danshu', DoctorTypes.PHYSICIAN)
doctor_bl.show_doctors()

patient_bl.add_patient('Shobha')
patient_bl.add_patient('Shobha')
patient_bl.add_patient('Manish')

doctor_bl.add_service_slot('Mashu', '9:00')
doctor_bl.add_service_slot('Mashu', '9:00')
doctor_bl.add_service_slot('Mashu', '10:00')
doctor_bl.add_service_slot('Mashum', '9:00')
doctor_bl.show_available_slots('Mashu')

booking_bl.add_booking('Mashu', 'Shobham', '9:00')
booking_bl.add_booking('Mashum', 'Shobha', '9:00')
booking_bl.add_booking('Mashu', 'Shobha', '9:00')
booking_bl.add_booking('Mashu', 'Shobha', '9:00')
booking_bl.add_booking('Mashu', 'Shobha', '9:30')
booking_bl.show_patient_bookings('Shobha')
booking_bl.show_patient_bookings('Manish')
booking_bl.show_doctor_bookings('Mashu')