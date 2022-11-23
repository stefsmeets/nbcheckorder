# nbcheckorder

Pre-commit hook to check the order of Jupyter notebook cells.

Prevents notebooks from being commited if the cell order is not sequential. This can avoid hidden state, or make sure that WIP notebooks are not commited by accident.

Try it out by running:

```bash
pre-commit try-repo https://github.com/stefsmeets/nbcheckorder/ --all-files
```

## Installing it as a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions.

Sample `.pre-commit-config.yaml`:

```yaml
  - repo: https://github.com/stefsmeets/nbcheckorder/
    rev: v0.2.0
    hooks:
      - id: nbcheckorder
```
