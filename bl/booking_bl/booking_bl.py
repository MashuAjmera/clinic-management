from bl.base_bl import BaseBl
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
        patient = None
        try:
            slot = Slot(slot_time)
            patient = self.patient_bl.book(patient_name, slot)
            doctor = self.doctor_bl.book(doctor_name, slot)
            self.bookings.append(Booking(doctor, patient, slot))
            print(f'Slot {slot_time} booked successfully for Patient {patient_name} and Dr. {doctor_name}.')
        except Exception as e:
            print(e)
            if patient:
                try:
                    self.patient_bl.cancel(patient_name, slot)
                except Exception as e:
                    print(e)

    def show_patient_bookings(self, name: str):
        print(f'Booking for patient {name} are:', end=' ')
        for booking in self.bookings:
            if booking.patient.name == name:
                print(f'Dr. {booking.doctor.name}-{booking.slot.time}', end=', ')
        print()

    def show_doctor_bookings(self, name: str):
        print(f'Booking for Dr. {name} are:', end=' ')
        for booking in self.bookings:
            if booking.doctor.name == name:
                print(f'{booking.patient.name}-{booking.slot.time}', end=', ')
        print()

    def cancel_booking(self, patient_name: str, doctor_name: str, slot_time: str) -> None:
        patient = None
        try:
            slot = Slot(slot_time)
            patient = self.patient_bl.cancel(patient_name, slot)
            doctor = self.doctor_bl.cancel(doctor_name, slot)
            for i, booking in enumerate(self.bookings):
                if booking.doctor == doctor and booking.patient == patient and booking.slot == slot:
                    self.bookings.pop(i)
                    break
            else:
                raise Exception(f'Booking for Dr. {doctor_name} with patient {patient_name} not available at {slot_time}.')
            print(f'Slot {slot_time} cancelled successfully for Patient {patient_name} and Dr. {doctor_name}.')
        except Exception as e:
            print(e)
            if patient:
                try:
                    self.patient_bl.cancel(patient_name, slot)
                except Exception as e:
                    print(e)