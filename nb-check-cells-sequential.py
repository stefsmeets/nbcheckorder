import argparse
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence
from typing import Tuple
import nbformat


def are_cells_sequential(filename):
    node = nbformat.read(filename, as_version=4)
    cells = node['cells']

    for i, cell in enumerate(cells):
        cell_number = int(cell['execution_count'])
        expected_number = i + 1

        if not cell_number == expected_number:
            return False

    return True


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        if not are_cells_sequential(filename):
            retval = 1

    return retval


if __name__ == '__main__':
    raise SystemExit(main())