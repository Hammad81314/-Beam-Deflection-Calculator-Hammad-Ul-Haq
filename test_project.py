
### 4. Full `test_project.py`

```python
import pytest
from project import calculate_deflection, get_numeric_input, calculate_bending_moment

@pytest.mark.parametrize("beam_type, load_type, P, w, L, E, I, expected", [
    ("simply_supported", "point_load", 1000, 0, 2, 200e9, 0.0001, 8.333333e-6),
    ("cantilever", "point_load", 1000, 0, 2, 200e9, 0.0001, 1.333333e-4),
])
def test_calculate_deflection(beam_type, load_type, P, w, L, E, I, expected):
    assert pytest.approx(calculate_deflection(beam_type, load_type, P, w, L, E, I), rel=1e-6) == expected


@pytest.mark.parametrize("beam_type, load_type, P, w, L, expected", [
    ("simply_supported", "point_load", 1000, 0, 2, 500.0),
    ("simply_supported", "uniformly_distributed", 0, 500, 2, 250.0),
    ("cantilever", "point_load", 1000, 0, 2, 2000.0),
    ("cantilever", "uniformly_distributed", 0, 500, 2, 1000.0),
])
def test_calculate_bending_moment(beam_type, load_type, P, w, L, expected):
    assert pytest.approx(calculate_bending_moment(beam_type, load_type, P, w, L), rel=1e-6) == expected


def test_get_numeric_input(monkeypatch):
    # Mock input for positive number
    monkeypatch.setattr('builtins.input', lambda _: "10")
    assert get_numeric_input("Enter a number: ") == 10.0

    # Mock input for negative number with positive_only=True
    monkeypatch.setattr('builtins.input', lambda _: "-10")
    with pytest.raises(ValueError):
        get_numeric_input("Enter a positive number: ", positive_only=True)


def test_invalid_beam_load_type():
    with pytest.raises(ValueError):
        calculate_deflection("invalid_beam", "point_load", 1000, 0, 2, 200e9, 0.0001)
    with pytest.raises(ValueError):
        calculate_deflection("cantilever", "invalid_load", 1000, 0, 2, 200e9, 0.0001)

    with pytest.raises(ValueError):
        calculate_bending_moment("invalid_beam", "point_load", 1000, 0, 2)
    with pytest.raises(ValueError):
        calculate_bending_moment("cantilever", "invalid_load", 1000, 0, 2)
