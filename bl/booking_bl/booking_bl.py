from bl.base_bl.base_bl import BaseBl
from bl.booking_bl.ibooking_bl import IBookingBl
from modals.booking import Booking
from modals.slot import Slot
from utilities.factory import Factory

class BookingBl(BaseBl, IBookingBl):
    def __init__(self):
        self.bookings = []
        self.doctor_bl = Factory.get_doctor_bl()
        self.patient_bl = Factory.get_patient_bl()

    def add_booking(self, doctor_name: str, patient_name: str, slot_time: str):
        try:
            # check if patient exists
            patient = self.patient_bl._get_patient(patient_name)
            if not patient:
                raise Exception(f'Patient {patient_name} is not registered.')

            # check if patient doesnt have any bookings
            for booking in self.bookings:
                if booking.patient.name == patient_name and booking.slot.time == slot_time:
                    raise Exception(f'Patient {patient_name} is not available at {slot_time}.')
                
            # check if doctor exists
            doctor = self.doctor_bl._get_doctor(doctor_name)
            if not doctor:
                raise Exception(f'Dr. {doctor_name} is not registered.')

            slot = Slot(slot_time)
            # check and book slot for doctor
            self.doctor_bl.add_booked_slot(doctor_name, slot)

            # book slot
            self.bookings.append(Booking(doctor, patient, slot))
            print(f'Slot {slot_time} booked successfully for Patient {patient_name} and Dr. {doctor_name}.')
        except Exception as e:
            print(e)

    def show_patient_bookings(self, name: str):
        print(f'Booking for patient {name} are:', end=' ')
        for booking in self.bookings:
            if booking.patient.name == name:
                print(f'Dr. {booking.doctor.name}-{booking.slot.time}', end=', ')
        print()

    def show_doctor_bookings(self, name: str):
        print(f'Booking for patient {name} are:', end=' ')
        for booking in self.bookings:
            if booking.doctor.name == name:
                print(f'Patient {booking.patient.name}-{booking.slot.time}', end=', ')
        print()