from ht2 import folder_creation
import pytest

@pytest.mark.parametrize(
    "name, expected1, expected2",
    [
        ('one_more_another_folder', 201, 200),
        ('one_more_another_folder', 409, 200),
        ('', 400, 400)
    ]
)
def test_folder_creation(name, expected1, expected2):
    assert folder_creation(name) == (expected1, expected2)
