"""Unit tests for cart_total.calculate_total.

Requirements tested (from the Project 01 specification):
- Total = unit price x quantity, returned in cents.
- A unit price or quantity of zero gives a total of zero.
- Non-int arguments (including bool) raise TypeError.
- Negative arguments raise ValueError.
"""
import pytest

from cart_total import calculate_total


# ---------- Valid inputs ----------
@pytest.mark.parametrize(
    "unit_price, quantity, expected",
    [
        (250, 3, 750),            # typical case
        (100, 1, 100),            # boundary: smallest non-zero quantity
        (1, 1, 1),                # boundary: smallest non-zero price and quantity
        (1000000, 1000, 1000000000),  # large values
    ],
)
def test_calculate_total_multiplies_price_by_quantity(unit_price, quantity, expected):
    assert calculate_total(unit_price, quantity) == expected


@pytest.mark.parametrize("quantity", [1, 5, 100])
def test_calculate_total_returns_zero_when_price_is_zero(quantity):
    assert calculate_total(0, quantity) == 0


@pytest.mark.parametrize("unit_price", [1, 500, 99999])
def test_calculate_total_returns_zero_when_quantity_is_zero(unit_price):
    # Spec: a quantity of zero results in a total of zero.
    assert calculate_total(unit_price, 0) == 0


def test_calculate_total_returns_zero_when_price_and_quantity_are_zero():
    assert calculate_total(0, 0) == 0


# ---------- Invalid types -> TypeError ----------
@pytest.mark.parametrize(
    "bad_price", [10.5, "100", None, True, False, [100]]
)
def test_calculate_total_rejects_invalid_price_type(bad_price):
    with pytest.raises(TypeError):
        calculate_total(bad_price, 2)


@pytest.mark.parametrize(
    "bad_quantity", [2.0, "2", None, True, False, [2]]
)
def test_calculate_total_rejects_invalid_quantity_type(bad_quantity):
    with pytest.raises(TypeError):
        calculate_total(100, bad_quantity)


# ---------- Out-of-range values -> ValueError ----------
@pytest.mark.parametrize("bad_price", [-1, -100])
def test_calculate_total_rejects_negative_price(bad_price):
    with pytest.raises(ValueError):
        calculate_total(bad_price, 2)


@pytest.mark.parametrize("bad_quantity", [-1, -10])
def test_calculate_total_rejects_negative_quantity(bad_quantity):
    with pytest.raises(ValueError):
        calculate_total(100, bad_quantity)# cancel test 1  
# cancel test 2  


paractise = 11