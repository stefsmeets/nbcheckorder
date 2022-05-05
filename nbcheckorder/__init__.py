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

    code_cells = [cell for cell in cells if cell['cell_type'] == 'code']

    for i, cell in enumerate(code_cells):
        cell_number = i + 1
        execution_count = cell.get('execution_count')

        if (execution_count is None) and not (cell_number == len(code_cells)):
            print(f'{filename}: Notebook contains unexecuted cells ({cell_number=})')
            return False
        else:
            execution_count = int(execution_count)

        if not execution_count == cell_number:
            print(f'{filename}: Notebook cells are out of order ({cell_number=}, {execution_count=})')
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
