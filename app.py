from utilities.factory import Factory
from constants.doctor_types import DoctorTypes

doctor_bl = Factory.get_doctor_bl()
patient_bl = Factory.get_patient_bl()
booking_bl = Factory.get_booking_bl()

doctor_bl.add('Mashu', DoctorTypes.PULMONOLOGIST)
doctor_bl.add('Danshu', DoctorTypes.PHYSICIAN)
doctor_bl.show_doctors()

patient_bl.add('Shobha')
patient_bl.add('Shobha')
patient_bl.add('Manish')

doctor_bl.add_service_slot('Mashu', '9:00')
doctor_bl.add_service_slot('Mashu', '9:00')
doctor_bl.add_service_slot('Mashu', '10:00')
doctor_bl.add_service_slot('Mashum', '9:00')
doctor_bl.add_service_slot('Danshu', '11:00')
doctor_bl.show_available_slots('Mashu')
doctor_bl.show_available_slots_by_type(DoctorTypes.PHYSICIAN)

booking_bl.add_booking('Mashu', 'Shobham', '9:00')
booking_bl.add_booking('Mashum', 'Shobha', '9:00')
booking_bl.add_booking('Mashu', 'Shobha', '9:00')
booking_bl.add_booking('Mashu', 'Shobha', '9:00')
booking_bl.add_booking('Mashu', 'Shobha', '9:30')
booking_bl.add_booking('Mashu', 'Shobha', '10:00')
booking_bl.show_patient_bookings('Shobha')
booking_bl.cancel_booking('Shobha', 'Mashu', '10:00')
booking_bl.show_patient_bookings('Manish')
booking_bl.show_doctor_bookings('Mashu')