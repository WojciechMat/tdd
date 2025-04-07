import pytest
from src.machine_power_calculator import MachinePowerCalculator, ArgumentException

class TestMachinePowerCalculator:
    
    @pytest.fixture
    def calculator(self):
        return MachinePowerCalculator()
    
    def test_empty_machine_type_raises_exception(self, calculator: MachinePowerCalculator):
        """Test that empty machine type raises an ArgumentException."""
        with pytest.raises(ArgumentException, match="Machine type cannot be empty"):
            calculator.GetPowerConsumption("", 10, False)

    def test_negative_duration_raises_exception(self, calculator: MachinePowerCalculator):
        with pytest.raises(ArgumentException, match="Duration must be greater than zero"):
            calculator.GetPowerConsumption("MillingMachine", -1, False)

    def test_unknown_machine_type_raises_exception(self, calculator: MachinePowerCalculator):
        with pytest.raises(ArgumentException, match="Invalid machine type"):
            calculator.GetPowerConsumption("UnknownMachine", 10, False)

    