# Example repo for https://github.com/pydantic/pydantic/issues/10970

This is a very simple example to reproduce the error, just need to have `uv` installed:

- `uv sync` to install both packages
- `uv run hello.py` to check that is running as expected
- `uv run mypy .` to check that mypy is raising an error

There is a branch `pydantic-2.9.2` to show that the error is not present in that version.
