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
            power = 5.0 * duration

        elif machineType == "Press":
            power = 7.2 * duration
    
        elif machineType == "Lathe":
            power = 3.5 * math.log10(duration + 1)
    
        else:
            raise ArgumentException("Invalid machine type")

        if isEnergySaving:
            power = power * 0.8
        
        return power
