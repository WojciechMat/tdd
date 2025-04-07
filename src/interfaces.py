from abc import ABC, abstractmethod


class IMachine(ABC):
    @abstractmethod
    def calculate_power_consumption(self, duration: int) -> float:
        pass


class IEnergySavingStrategy(ABC):
    @abstractmethod
    def apply(self, power: float) -> float:
        pass
