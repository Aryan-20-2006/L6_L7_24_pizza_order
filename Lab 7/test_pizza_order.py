from hypothesis import given, strategies as st
from pizza_order import toppings_price, pizza_inches, split_bill

@given(st.text() | st.none())
def test_toppings_price_no_crash(s):

@given(st.text() | st.none())
def test_pizza_inches_no_crash(s):

@given(st.text() | st.none())
def test_split_bill_no_crash(s):
