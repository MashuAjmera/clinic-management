from abc import abstractmethod
from typing import List

from bl.ibase_bl import IBaseBl
from modals.entity import Entity
from modals.slot import Slot


class IEntityBl(IBaseBl):

    @abstractmethod
    def add(self, name: str) -> None:
        pass

    @abstractmethod
    def get(self, name: str) -> Entity:
        pass

    @abstractmethod
    def book(self, name: str, slot: Slot) -> Entity:
        pass

    @abstractmethod
    def cancel(self, name: str, slot: Slot) -> None:
        pass

    @abstractmethod
    def _check_availability(self, entity: Entity, slot: Slot) -> None:
        pass