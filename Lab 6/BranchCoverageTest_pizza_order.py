import pytest
from pizza_order import pizza_price, order_discount, delivery_status

# Test cases chosen so that every decision in pizza_order.py evaluates to
# both True and False, including the boundary values of each comparison.


# pizza_price
# Branch: size not in SIZE_PRICE -> True / False
def test_unknown_size_raises():
    with pytest.raises(ValueError, match="unknown size"):
        pizza_price("extra large", 1, False)

def test_plain_medium_pizza():
    assert pizza_price("medium", 0, False) == 350

# Branch: toppings < 0 -> True / False
def test_negative_toppings_raises():
    with pytest.raises(ValueError, match="invalid toppings"):
        pizza_price("medium", -1, False)

# Branch: toppings > 3 -> False (boundary 3) / True (boundary 4)
def test_three_toppings_charged_at_full_rate():
    assert pizza_price("small", 3, False) == 200 + 3 * 40

def test_four_toppings_extra_at_reduced_rate():
    assert pizza_price("small", 4, False) == 200 + 3 * 40 + 30

# Branch: is_cheese_burst -> True / False, size == "small" -> True / False
def test_large_many_toppings_cheese_burst():
    assert pizza_price("large", 5, True) == 500 + 3 * 40 + 2 * 30 + 100

def test_medium_cheese_burst():
    assert pizza_price("medium", 2, True) == 350 + 2 * 40 + 100

def test_small_cheese_burst_raises():
    with pytest.raises(ValueError, match="cheese burst not available for small"):
        pizza_price("small", 1, True)


# order_discount
# Branch: order_total < 300 -> True (boundary 299) / False (boundary 300)
def test_order_below_minimum_gets_no_discount():
    assert order_discount(299, "tuesday", True) == 0

def test_order_at_minimum_gets_discount():
    assert order_discount(300, "monday", False) == 30

# Branch: day == "tuesday" / day in weekend / any other day,
# each with is_student True and False
def test_tuesday_student_discount():
    assert order_discount(400, "tuesday", True) == 250

def test_tuesday_non_student_discount():
    assert order_discount(400, "tuesday", False) == 200

def test_saturday_non_student_no_discount():
    assert order_discount(400, "saturday", False) == 0

def test_sunday_student_discount():
    assert order_discount(400, "sunday", True) == 50

def test_weekday_student_discount():
    assert order_discount(400, "monday", True) == 90

def test_weekday_non_student_discount():
    assert order_discount(400, "friday", False) == 40


# delivery_status
# Branch: distance_km > 10 -> True (boundary 11) / False (boundary 10)
def test_too_far_not_deliverable():
    assert delivery_status(20, 11) == "not deliverable"

def test_max_distance_deliverable():
    assert delivery_status(20, 10) == "on time"

# Branch: minutes_taken <= 30 -> True / False, minutes_taken <= 45 -> True / False
def test_on_time_delivery():
    assert delivery_status(20, 3) == "on time"

def test_exactly_30_minutes_on_time():
    assert delivery_status(30, 3) == "on time"

def test_late_delivery():
    assert delivery_status(31, 3) == "late"

def test_exactly_45_minutes_late():
    assert delivery_status(45, 3) == "late"

def test_very_late_delivery_free_pizza():
    assert delivery_status(46, 3) == "free pizza"
