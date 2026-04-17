from typing import Literal

INT_LIMIT = 999_999_999


def _validate_args(number: int, gender: Literal["M", "F"], plural: bool, before_noun: bool) -> None:
    if not isinstance(number, int):
        raise TypeError(f"number must be an int, got {type(number).__name__}")
    if number <= 0:
        raise ValueError(f"number must be a positive integer, got {number}")
    if number > INT_LIMIT:
        raise ValueError(f"number must be <= {INT_LIMIT:,}, got {number}")
    if not isinstance(gender, str) or gender not in ("M", "F"):
        raise ValueError(f"gender must be 'M' or 'F', got {gender!r}")
    if not isinstance(plural, bool):
        raise TypeError(f"plural must be a bool, got {type(plural).__name__}")
    if not isinstance(before_noun, bool):
        raise TypeError(
            f"before_noun must be a bool, got {type(before_noun).__name__}")


def _can_apocopate(n: int) -> bool:
    "Wether n can be apocopated (supress sound at the end)."
    if n in (1, 3, 13):
        return True
    if 20 <= n <= 99:
        return n % 10 in (1, 3)
    if 100 <= n <= 999:
        return _can_apocopate(n % 100)
    if 1_000 <= n <= 999_999:
        return _can_apocopate(n % 1000)
    if 1_000_000 <= n <= 999_999_999:
        return _can_apocopate(n % 1_000_000)
    return False


def _affix(n: int, g: Literal["M", "F"], p: bool = False, bn: bool = False) -> str:
    "Affix of n, with g genre and p plurality."

    if p:
        return _affix(n, g, p=False, bn=False) + "s"
    elif g == "M":
        if bn and _can_apocopate(n):
            return ""
        else:
            return "o"
    else:
        return "a"


def _root(n: int, g: Literal["M", "F"], p: bool = False) -> str:
    "Root part of n with g gender and p plurality."

    match n:
        case 1:
            return "primer"
        case 2:
            return "segund"
        case 3:
            return "tercer"
        case 4:
            return "cuart"
        case 5:
            return "quint"
        case 6:
            return "sext"
        case 7:
            return "séptim"
        case 8:
            return "octav"
        case 9:
            return "noven"
            # Also nono, nona
        case 10:
            return "décim"
            # Also decen
        case 11:
            return "undécim"
            # Also oncen
            # Also decimoprimer
            # Also décimo primero, décima primera
        case 12:
            return "duodécim"
            # Also dozen
            # Also decimosegund
            # Also décimo segundo, décima segunda
        # Some excluded forms:
        # 13: Also trecen
        # 13: Also tredécim
        # 14: Also catorcen
        # 14: Also catorzen
        # 15: Also quincen
        # 16: Also dieciseisen
        # 17: Also decimosétim
        # 18: Also deciochen
        case 20:
            return "vigésim"
        case 30:
            return "trigésim"
        case 40:
            return "cuadrigésim"
        case 50:
            return "quincuagésim"
        case 60:
            return "sexagésim"
        case 70:
            return "septuagésim"
        case 80:
            return "octogésim"
        case 90:
            return "nonagésim"
        case 100:
            return "centésim"
        case 200:
            return "duocentésim"
        case 300:
            return "tricentésim"
        case 400:
            return "cuadrigentésim"
        case 500:
            return "quingentésim"
        case 600:
            return "sexgentésim"
        case 700:
            return "septingentésim"
        case 800:
            return "octigentésim"
        case 900:
            return "noningentésim"
        case 1000:
            return "milésim"
        case 2000:
            return "dosmilésim"
        case 3000:
            return "tresmilésim"
        case 4000:
            return "cuatromilésim"
        case 5000:
            return "cincomilésim"
        case 6000:
            return "seismilésim"
        case 7000:
            return "sietemilésim"
        case 8000:
            return "ochomilésim"
        case 9000:
            return "nuevemilésim"
        case 1_000_000:
            return "millonésim"
    if 13 <= n <= 19:
        return "decimo" + _root(n % 10, g, p)
        # Also,their variants with "décimo" (instead of "decimo") and the number separated with a withespace.
    if 21 <= n <= 99:
        return (
            intesim((n // 10) * 10, g, p, before_noun=True)
            + " "
            + _root(n % 10, g, p)
        )
    if 101 <= n <= 999:
        return (
            intesim((n // 100) * 100, g, p, before_noun=True)
            + " "
            + _root(n - (n // 100) * 100, g, p)
        )
    if 1001 <= n <= 999_999:
        if n % 1000 == 0:
            return (
                intesim(n // 1000, g, p, before_noun=True)
                + " "
                + _root(1000, g, p)
            )
        else:
            return (
                intesim((n // 1000) * 1000, g,
                        p, before_noun=True)
                + " "
                + _root(n - (n // 1000) * 1000, g, p)
            )
    if 1_000_001 <= n <= 999_999_999:
        if n % 1_000_000 == 0:
            return (
                intesim(n // 1_000_000, g, p, before_noun=True)
                + " "
                + _root(1_000_000, g, p)
            )
        else:
            return (
                intesim((n // 1_000_000) * 1_000_000,
                        g, p, before_noun=True)
                + " "
                + _root(n - (n // 1_000_000)
                        * 1_000_000, g, p)
            )

    raise NotImplementedError(f"Ordinal not implemented for {n}")


def intesim(number: int, gender: Literal["M", "F"], plural=False, before_noun=False) -> str:
    """Positive integer in the Spanish "ésim" ordnial notation.

    Args:
        number (int): positive integer.
        gender (str): "M" for masculine, or "F" for femenine genre.
        plural (bool, optional): plurality of the ordinal. Defaults to False.
        before_noun (bool, optional): wheter the string comes before a noun. Defaults to False.

    Returns:
        str: "number" in the Spanish "ésim" ordinal notation, with "gender" gender and "plural" plurality.
    """
    _validate_args(number, gender, plural, before_noun)

    return _root(number, gender, plural) + _affix(number, gender, plural, before_noun)


if __name__ == "__main__":
    from random import randint
    print("-" * 18)
    print(f"El Entero Es Ésimo")
    print("-" * 18)
    NUMS = (randint(1, 9), randint(10, 99), randint(100, 999),
            randint(1_000, 9_999), randint(10_000, 99_999),
            randint(100_000, 999_999), randint(1_000_000, 9_999_999),
            randint(10_000_000, 99_999_999),
            randint(100_000_000, 999_999_999))
    for a in NUMS:
        print(f"{a}:{" " * (10 - len(str(a)))}{
            intesim(a,
                    gender=("M", "F")[randint(0, 1)],
                    plural=(True, False)[randint(0, 1)],
                    before_noun=(True, False)[randint(0, 1)]
                    )}"
              )
