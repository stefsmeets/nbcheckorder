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
        execution_count = int(cell['execution_count'])
        cell_number = i + 1

        if not execution_count == cell_number:
            return False

    return True


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    retval = 0

    for filename in args.filenames:
        if not are_cells_sequential(filename):
            print(f'{filename}: Notebook cells are out of order')
            retval = 1

    return retval


if __name__ == '__main__':
    raise SystemExit(main())