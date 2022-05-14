from calculatorlibrary import __version__
from calculatorlibrary.arithmetics import add


class TestCalculator:
    def test_version(self):
        assert __version__ == "0.1.0"

    def test_add_function(self, args=[2, 3, 4, 5, 6]):
        assert add(*args) == 20
