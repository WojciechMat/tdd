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