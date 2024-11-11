from nbcheckorder import are_cells_sequential, are_all_cells_unexecuted
import pytest
from pathlib import Path

TESTS_DIR = Path(__file__).parent


@pytest.mark.parametrize("filename,expected_result", 
(
    (TESTS_DIR / 'dirty_order.ipynb', False),
    (TESTS_DIR / 'clean_order.ipynb', True),
    (TESTS_DIR / 'unexecuted.ipynb', False),
))

def test_are_cells_sequential(filename, expected_result):
    result = are_cells_sequential(filename)

    assert result == expected_result

@pytest.mark.parametrize("filename,expected_result", 
(
    (TESTS_DIR / 'dirty_order.ipynb', False),
    (TESTS_DIR / 'clean_order.ipynb', False),
    (TESTS_DIR / 'unexecuted.ipynb', True),
))

def test_are_all_cells_unexecuted(filename, expected_result):
    result = are_all_cells_unexecuted(filename)

    assert result == expected_result

