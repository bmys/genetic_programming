from abc import ABC, abstractmethod


class Vm(ABC):
    @abstractmethod
    def reset(self):
        ...

    @abstractmethod
    def execute(self, program):
        ...

    @property
    @abstractmethod
    def get_program(self):
        ...

    @property.setter
    @abstractmethod
    def get_program(self):
        ...
