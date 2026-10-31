import pytest
from pizza_order import pizza_price, order_discount, delivery_status

# Test cases chosen so that every line of pizza_order.py executes at least once.


# pizza_price
def test_plain_medium_pizza():
    assert pizza_price("medium", 0, False) == 350

def test_unknown_size_raises():
    with pytest.raises(ValueError, match="unknown size"):
        pizza_price("extra large", 1, False)

def test_negative_toppings_raises():
    with pytest.raises(ValueError, match="invalid toppings"):
        pizza_price("medium", -1, False)

def test_large_many_toppings_cheese_burst():
    # 500 + 3*40 + 2*30 + 100
    assert pizza_price("large", 5, True) == 780

def test_small_cheese_burst_raises():
    with pytest.raises(ValueError, match="cheese burst not available for small"):
        pizza_price("small", 1, True)


# order_discount
def test_order_below_minimum_gets_no_discount():
    assert order_discount(200, "monday", True) == 0

def test_tuesday_student_discount():
    assert order_discount(400, "tuesday", True) == 250

def test_weekend_student_discount():
    assert order_discount(400, "sunday", True) == 50

def test_weekday_student_discount():
    assert order_discount(400, "monday", True) == 90


# delivery_status
def test_on_time_delivery():
    assert delivery_status(20, 3) == "on time"

def test_too_far_not_deliverable():
    assert delivery_status(20, 15) == "not deliverable"

def test_late_delivery():
    assert delivery_status(40, 3) == "late"

def test_very_late_delivery_free_pizza():
    assert delivery_status(50, 3) == "free pizza"
