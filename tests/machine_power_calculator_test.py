import pytest

from src.machine_power_calculator import ArgumentException, MachinePowerCalculator


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

    def test_milling_machine_power_consumption(self, calculator: MachinePowerCalculator):
        assert calculator.GetPowerConsumption("MillingMachine", 1, False) == 5.0
        assert calculator.GetPowerConsumption("MillingMachine", 10, False) == 50.0
        assert calculator.GetPowerConsumption("MillingMachine", 50, False) == 250.0

    def test_press_power_consumption(self, calculator: MachinePowerCalculator):
        assert calculator.GetPowerConsumption("Press", 1, False) == 7.2
        assert calculator.GetPowerConsumption("Press", 10, False) == 72.0

    def test_lathe_power_consumption(self, calculator: MachinePowerCalculator):
        assert round(calculator.GetPowerConsumption("Lathe", 1, False), 2) == 1.05
        assert round(calculator.GetPowerConsumption("Lathe", 2, False), 2) == 1.67
        assert round(calculator.GetPowerConsumption("Lathe", 10, False), 2) == 3.64
        assert round(calculator.GetPowerConsumption("Lathe", 100, False), 2) == 7.02

    def test_energy_saving_mode(self, calculator: MachinePowerCalculator):
        assert calculator.GetPowerConsumption("MillingMachine", 1, True) == 4.0
        assert pytest.approx(calculator.GetPowerConsumption("Press", 1, True)) == 5.76
        assert round(calculator.GetPowerConsumption("Lathe", 1, True), 2) == 0.84
        assert calculator.GetPowerConsumption("MillingMachine", 10, True) == 40.0
