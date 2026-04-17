import pytest
from intesim import intesim


# --- Basic singular forms ---


def test_first_masculine() -> None:
    assert intesim(1, "M") == "primero"


def test_first_feminine() -> None:
    assert intesim(1, "F") == "primera"


def test_first_no_genre() -> None:
    assert intesim(1) == "primero"  # defaults to "o"


def test_third_no_genre() -> None:
    # 3rd has special rule: no genre letter when genre is None
    assert intesim(3) == "tercer"


def test_tenth_masculine() -> None:
    assert intesim(10, "M") == "décimo"


# --- Plural forms ---


def test_first_masculine_plural() -> None:
    assert intesim(1, "M", p=True) == "primeros"


def test_first_feminine_plural() -> None:
    assert intesim(1, "F", p=True) == "primeras"


# --- Compound numbers ---


def test_twenty_first_feminine() -> None:
    assert intesim(21, "F") == "vigésima primera"


def test_one_hundred_masculine() -> None:
    assert intesim(100, "M") == "centésimo"


def test_one_thousand_feminine() -> None:
    assert intesim(1000, "F") == "milésima"


# --- Invalid inputs raise AssertionError ---


def test_rejects_zero() -> None:
    with pytest.raises(AssertionError):
        intesim(0)


def test_rejects_negative() -> None:
    with pytest.raises(AssertionError):
        intesim(-5)


def test_rejects_invalid_genre() -> None:
    with pytest.raises(AssertionError):
        intesim(1, "X")


def test_rejects_non_integer() -> None:
    with pytest.raises(AssertionError):
        intesim(1.5)


# --- Parametrized tests for a range of values ---


@pytest.mark.parametrize(
    "n,genre,expected",
    [
        (2, "M", "segundo"),
        (2, "F", "segunda"),
        (5, "M", "quinto"),
        (12, "F", "duodécima"),
        (20, "M", "vigésimo"),
        (1000, "M", "milésimo"),
    ],
)
def test_parametrized(n, genre, expected) -> None:
    assert intesim(n, genre) == expected
