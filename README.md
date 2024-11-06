# clinic-management
Low Level Backend System Design of Clinic Booking Management System.

## Entities
- Entity
  - Doctor
  - Patient
- Booking
- Slot

## Design Patterns
### Creational Patterns
- **Singleton**: Doctor, Patient are singleton classes since all the information has to be preserved.
- **Factory**: Factory class gives the respective Bl.required
### Structural Patterns
- **Adapter**: EntityBl adds an entity to the entity list depending on the eype of entity passed.
- **Facade**: BookingBl provides an interface to book both doctors and patients together.