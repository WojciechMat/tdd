class ArgumentException(Exception):
    pass

class MachinePowerCalculator:
    
    def GetPowerConsumption(self, machineType: str, duration: int, isEnergySaving: bool,):
        if not machineType:
            raise ArgumentException("Machine type cannot be empty")
            
        if duration < 0:
            raise ArgumentException("Duration must be greater than zero")
            
        valid_machine_types = ["MillingMachine", "Press", "Lathe"]
        if machineType not in valid_machine_types:
            raise ArgumentException("Invalid machine type")
            
        if machineType == "MillingMachine":
            return 5.0
            
        return 0.0