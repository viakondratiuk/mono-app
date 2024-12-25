import pytest

from main import adder


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (2, 3, 5),
        (3, 4, 7),
    ],
)
def test_adder(a: int, b: int, expected: int) -> None:
    assert adder(a, b) == expected
