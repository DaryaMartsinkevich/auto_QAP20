import pytest

from lesson_19.src.shop import Shop


@pytest.fixture
def shop():
    return Shop()