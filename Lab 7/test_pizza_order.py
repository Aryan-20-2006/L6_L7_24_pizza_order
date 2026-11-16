from hypothesis import given, strategies as st
from pizza_order import toppings_price, pizza_inches, split_bill

# Fuzz tests: feed arbitrary text (and None) into each function.
# The only acceptable failure is a ValueError, i.e. a deliberate, clean
# rejection of bad input. Any other exception (KeyError, TypeError,
# AttributeError, ZeroDivisionError, ...) is a crash and fails the test.


@given(st.text() | st.none())
def test_toppings_price_no_crash(s):
    try:
        result = toppings_price(s)
    except ValueError:
        return
    assert isinstance(result, int) and result > 0


@given(st.text() | st.none())
def test_pizza_inches_no_crash(s):
    try:
        result = pizza_inches(s)
    except ValueError:
        return
    assert result in (8, 10, 12)


@given(st.text() | st.none())
def test_split_bill_no_crash(s):
    try:
        result = split_bill(s)
    except ValueError:
        return
    assert isinstance(result, float) and result >= 0
