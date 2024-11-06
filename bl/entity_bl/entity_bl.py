from typing import List
from bl.base_bl import BaseBl
from bl.entity_bl.ientity_bl import IEntityBl
from modals.entity import Entity
from modals.slot import Slot

class EntityBl(BaseBl, IEntityBl):

    def __init__(self):
        self.entities = []

    def add(self, name: str, type: Entity = Entity) -> None:
        try:
            if self.get(name):
                raise Exception(f'Patient {name} already exists')
            self.entities.append(type(name))
            print(f'Welcome Dr. {name}!')
        except Exception as e:
            print(e)

    def get(self, name) -> Entity:
        for entity in self.entities:
            if entity.name == name:
                return entity
        return None
    
    def book(self, name: str, slot: Slot) -> Entity:
        try:
            entity = self.get(name)
            if not entity:
                raise Exception(f'Dr. {name} is not registered.')
            self._check_availability(entity, slot)
            entity.booked_slots.add(slot)
            return entity
        except Exception as e:
            raise
    
    def cancel(self, name: str, slot: Slot) -> Entity:
        try:
            entity = self.get(name)
            if not entity:
                raise Exception(f'Dr. {name} is not registered.')
            if slot not in entity.booked_slots:
                raise Exception(f'Dr. {name} has no slot booked at {slot.time}.')
            entity.booked_slots.remove(slot)
            return entity
        except Exception as e:
            raise
    
    def _check_availability(self, entity: Entity, slot: Slot) -> None:
        raise NotImplementedError("Subentities must implement this method")