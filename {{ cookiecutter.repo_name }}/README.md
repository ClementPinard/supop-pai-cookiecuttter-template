# {{ cookiecutter.project_full_name }}

This project was started with [supopo-pai-cookiecutter-template](https://github.com/ClementPinard/supop-pai-cookiecuttter-template/tree/main)

## How to run

```bash
uv run main
```

## How to run tests

```bash
uv sync --with test
uv run pytest
```

## How to build docs

```bash
uv sync --with docs
cd docs && make html
```

### How to run autobuild for docs

```bash
uv sync --with docs
cd docs && make livehtml
