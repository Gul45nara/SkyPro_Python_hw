from pages.calculator_page import CalculatorPage


def test_calculator_addition():
    """Test calculator addition operation"""
    calculator = CalculatorPage()
    result = calculator.add(5, 3)
    assert result == 8, f"Expected 8, but got {result}"


def test_calculator_subtraction():
    """Test calculator subtraction operation"""
    calculator = CalculatorPage()
    result = calculator.subtract(10, 4)
    assert result == 6, f"Expected 6, but got {result}"


def test_calculator_multiplication():
    """Test calculator multiplication operation"""
    calculator = CalculatorPage()
    result = calculator.multiply(7, 6)
    assert result == 42, f"Expected 42, but got {result}"


def test_calculator_division():
    """Test calculator division operation"""
    calculator = CalculatorPage()
    result = calculator.divide(15, 3)
    assert result == 5, f"Expected 5, but got {result}"


def test_calculator_division_by_zero():
    """Test calculator division by zero handling"""
    calculator = CalculatorPage()
    result = calculator.divide(10, 0)
    expected_msg = "Cannot divide by zero"
    assert result == expected_msg, (
        f"Expected '{expected_msg}', but got '{result}'"
    )
