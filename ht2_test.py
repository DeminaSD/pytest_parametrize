from ht2 import folder_creation
import pytest

@pytest.mark.parametrize(
    "name, expected1, expected2",
    [
        ('one_more_another_folder', 201, True),
        ('one_more_another_folder', 409, True),
        ('', 400, False)
    ]
)
# Если запрос был обработан без ошибок, API отвечает кодом 201 Created (папка успешно создана), 
# поэтому проверяется код 201
def test_folder_creation(name, expected1, expected2):
    assert folder_creation(name) == (expected1, expected2)
