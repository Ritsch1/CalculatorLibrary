from calculatorlibrary import __version__
from calculatorlibrary.arithmetics import add
import pytest


class TestCalculator:
    # Follow DRY pattern by providing and reusing test data for multiple functions
    @pytest.fixture
    def sample_numeric_data(self):
        return {
            "Addition_Subtraction": [
                ((1, 1, 2), 4, -2),
                ((2, 78, 43), 123, -119),
                ((-2, 10, 22), 30, -14),
            ]
        }

    def test_version(self):
        assert __version__ == "0.1.0"

    def test_add_function(self, sample_numeric_data):
        for args, result, _ in sample_numeric_data["Addition_Subtraction"]:
            assert add(*args) == result
