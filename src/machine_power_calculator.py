import math

from src.interfaces import IMachine, IEnergySavingStrategy


class ArgumentException(Exception):
    pass


class MillingMachine(IMachine):
    def calculate_power_consumption(self, duration: int) -> float:
        return 5.0 * duration


class Press(IMachine):
    def calculate_power_consumption(self, duration: int) -> float:
        return 7.2 * duration


class Lathe(IMachine):
    def calculate_power_consumption(self, duration: int) -> float:
        return 3.5 * math.log10(duration + 1)


class MachineFactory:
    @staticmethod
    def create_machine(machine_type: str) -> IMachine:
        if machine_type == "MillingMachine":
            return MillingMachine()
        elif machine_type == "Press":
            return Press()
        elif machine_type == "Lathe":
            return Lathe()
        else:
            raise ArgumentException(f"Invalid machine type: {machine_type}")


class StandardEnergySavingStrategy(IEnergySavingStrategy):
    def apply(self, power: float) -> float:
        return power * 0.8


class NoEnergySavingStrategy(IEnergySavingStrategy):
    def apply(self, power: float) -> float:
        return power


class InputValidator:
    @staticmethod
    def validate_machine_type(machine_type: str) -> None:
        if not machine_type:
            raise ArgumentException("Machine type cannot be empty")

    @staticmethod
    def validate_duration(duration: int) -> None:
        if duration <= 0:
            raise ArgumentException("Duration must be greater than zero")


class MachinePowerCalculator:
    def __init__(self):
        self.machine_factory = MachineFactory()
        self.validator = InputValidator()

    def GetPowerConsumption(
        self,
        machineType: str,
        duration: int,
        isEnergySaving: bool,
    ) -> float:
        self.validator.validate_machine_type(machineType)
        self.validator.validate_duration(duration)

        machine = self.machine_factory.create_machine(machineType)

        power = machine.calculate_power_consumption(duration)

        energy_strategy = StandardEnergySavingStrategy() if isEnergySaving else NoEnergySavingStrategy()
        power = energy_strategy.apply(power)

        return power
