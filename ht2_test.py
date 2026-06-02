from ht2 import folder_creation
import pytest

@pytest.mark.parametrize(
    "name, expected",
    [
        ('one_more_another_folder', '<Response [201]>'),
        ('', '<Response [400]>')
    ]
)
def test_folder_creation(name, expected):
    assert folder_creation(name) == expected