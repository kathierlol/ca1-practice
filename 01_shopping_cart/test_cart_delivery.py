"""Unit tests for cart_delivery.qualifies_free_delivery.

Requirements tested (from the Project 01 specification):
- Totals of S$50.00 (5000 cents) or more qualify for free delivery (True).
- Totals below S$50.00 do not qualify (False).
- Non-int arguments (including bool) raise TypeError.
- Negative totals raise ValueError.
"""
import pytest

from cart_delivery import qualifies_free_delivery


# ---------- Below the threshold -> False ----------
@pytest.mark.parametrize("total_cents", [0, 1, 2500, 4999])
def test_total_below_5000_does_not_qualify(total_cents):
    assert qualifies_free_delivery(total_cents) is False


# ---------- At or above the threshold -> True ----------
def test_total_exactly_5000_qualifies():
    # Boundary: spec says S$50.00 OR MORE qualifies.
    assert qualifies_free_delivery(5000) is True


@pytest.mark.parametrize("total_cents", [5001, 10000, 1000000])
def test_total_above_5000_qualifies(total_cents):
    assert qualifies_free_delivery(total_cents) is True


# ---------- Invalid types -> TypeError ----------
@pytest.mark.parametrize(
    "bad_total", [5000.0, "5000", None, True, False, [5000]]
)
def test_invalid_total_type_raises_type_error(bad_total):
    with pytest.raises(TypeError):
        qualifies_free_delivery(bad_total)


# ---------- Out-of-range values -> ValueError ----------
@pytest.mark.parametrize("bad_total", [-1, -5000])
def test_negative_total_raises_value_error(bad_total):
    with pytest.raises(ValueError):
        qualifies_free_delivery(bad_total)





        #Test 
        # change 2