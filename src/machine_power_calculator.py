import math

class ArgumentException(Exception):
    pass


class MachinePowerCalculator:
    def GetPowerConsumption(
        self,
        machineType: str,
        duration: int,
        isEnergySaving: bool,
    ):
        if not machineType:
            raise ArgumentException("Machine type cannot be empty")

        if duration <= 0:
            raise ArgumentException("Duration must be greater than zero")

        if machineType == "MillingMachine":
            return 5.0 * duration

        elif machineType == "Press":
            return 7.2 * duration
        
        elif machineType == "Lathe":
            return 3.5 * math.log10(duration + 1)

        else:
            raise ArgumentException("Invalid machine type")
