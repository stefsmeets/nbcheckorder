from nbcheckorder import are_cells_sequential
import pytest
from pathlib import Path

TESTS_DIR = Path(__file__).parent


@pytest.mark.parametrize("filename,expected_result", 
(
    (TESTS_DIR / 'dirty_order.ipynb', False),
    (TESTS_DIR / 'clean_order.ipynb', True),
))

def test_are_cells_sequential(filename, expected_result):
    result = are_cells_sequential(filename)

    assert result == expected_result