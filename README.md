# intesim

**intesim** converts positive integers into their Spanish ordinal form using the *ésimo/ésima* notation.

```python
from intesim import intesim

intesim(5, "M")           # → "quinto"
intesim(5, "F")           # → "quinta"
intesim(21, "M", True)    # → "vigésimos primeros"
intesim(1000, "F")        # → "milésima"
```
Requires Python 3.10 or higher.

<!--Wish we're able to do this:

---

## Installation

```bash
pip install intesim
```

---

-->

## Usage

```python
intesim(number: int, gender: Literal ["M", "F"], plural: bool=False, before_noun: bool=False)
```

### Parameters

| Parameter | Type          | Description                                                   |
| --------- | ------------- | ------------------------------------------------------------- |
| `number`       | `int`         | A positive integer to convert.                                |
| `gender`   | `"M" or "F"` | `"M"` for masculine, `"F"` for feminine form.                 |
| `plural`       | `bool`        | `True` for plural, `False` for singular. Defaults to `False`. |
| `before_noun`       | `bool`        | `True` for apocopated forms of some numbers, `False` for general forms. Defaults to `False`. |

### Returns

A `str` with the ordinal representation of `number`.

---

## Examples

### Gender

```python
intesim(1, "M")     # → "primero"
intesim(1, "F")     # → "primera"

intesim(3, "M")     # → "tercero"
intesim(3, "F")     # → "tercera"
```

### Plurality

```python
intesim(2, "M", True)    # → "segundos"
intesim(2, "F", True)    # → "segundas"
```

### Before Noun

(Only changes when masculine singular form)

```python
intesim(1, "M", False, False)   # → "primero"
intesim(3, "M", False, False)   # → "tercero"
intesim(13, "M", False, False)  # → "decimotercero"

intesim(1, "M", False, True)   # → "primer"
intesim(3, "M", False, True)   # → "tercer"
intesim(13, "M", False, True)  # → "decimotercer"
```

### Larger numbers

```python
intesim(20, "F")          # → "vigésima"
intesim(35, "M")          # → "trigésimo quinto"
intesim(100, "F")         # → "centésima"
intesim(451, "M")         # → "cuadrigentésimo quincuagésimo primero"
intesim(1000, "F", True)  # → "milésimas"
intesim(5000, "M")        # → "cincomilésimo"
```

```python
intesim(123_456_789, "F", True)  # → "centésimas vigésimas terceras millonésimas cuadrigentésimas quincuagésimas sextas milésimas septingentésimas octogésimas novenas"
intesim(333_333_333, "M", False)  # → "tricentésimo trigésimo tercer millonésimo tricentésimo trigésimo tercer milésimo tricentésimo trigésimo tercero"
```
This library currently covers ordinals from **1 to 999 999 999**.

For integers beyond the current cover of this library, the function raises a `ValueError`.

---

## Background

Spanish ordinals agree with the noun they modify in both **gender** (_-o_ / _-a_) and **number** (_-os_ / _-as_). The *ésimo* family of ordinals is the standard form for numbers above twelve and is used in formal, technical, and academic writing. For casual writing, the _-avo_/_-ava_ form is more common.

For some approved examples of this kind of spanish ordinals, look at the "Ordinales" column [here](https://www.rae.es/buen-uso-espa%C3%B1ol/tabla-de-numerales).

Apocopated versions of the ordinals are used only before masculine nouns. The RAE explains this more thoroughly [here](https://www.rae.es/dpd/ordinales#:~:text=vig%C3%A9simo%20segundas.-,4.,-Los%20ordinales%20primero).

---

## License

Apache 2.0
