from calculatorlibrary import __version__
from calculatorlibrary.arithmetics import add, subtract
import pytest


class TestCalculator:
    # DRY pattern by providing and reusing test data for multiple functions
    @pytest.fixture
    def sample_numeric_data(self):
        return {
            "Addition_Subtraction": [
                ((1, 1, 2), 4, -2),
                ((2, 78, 43), 123, -119),
                ((-2, 10, 22), 30, -34),
            ]
        }

    def test_version(self):
        assert __version__ == "0.1.0"

    @pytest.mark.module_functions
    def test_add_function(self, sample_numeric_data):
        for args, result, _ in sample_numeric_data["Addition_Subtraction"]:
            assert add(*args) == result

    @pytest.mark.module_functions
    def test_subtract_function(self, sample_numeric_data):
        for args, _, result in sample_numeric_data["Addition_Subtraction"]:
            assert subtract(*args) == result
