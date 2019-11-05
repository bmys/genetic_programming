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
    def program(self):
        ...

    @program.setter
    @abstractmethod
    def program(self, p):
        ...
