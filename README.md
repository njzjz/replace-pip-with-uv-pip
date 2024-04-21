# Replace pip with uv pip

[![PyPI](https://img.shields.io/pypi/v/replace-pip-with-uv-pip.svg)](https://pypi.org/project/replace-pip-with-uv-pip)

A simple script to replace [`pip`](https://github.com/pypa/pip) with [`uv pip`](https://github.com/astral-sh/uv). Note that `pip` and `uv pip` have [many differences](https://github.com/astral-sh/uv/blob/main/PIP_COMPATIBILITY.md).

Although [pip maintainers are strongly against providing `pip` -> `uv pip` alias](https://github.com/astral-sh/uv/issues/1331#issuecomment-1947355046), it's still valuable in several use cases, especially in the CI service (see below).

## Use cases

### cibuildwheel

When using [cibuildwheel](https://github.com/pypa/cibuildwheel/), the hardcoded [`pip install`](https://github.com/pypa/cibuildwheel/blob/9cf99e78bc06d33fb2947de5820be96ad9c7152c/cibuildwheel/linux.py#L349-L352) is called when testing a wheel.
There is no way to replace `pip install` with `uv pip install` on the user side.
Installing `replace-pip-with-uv-pip` is a workaround:

```toml
# in pyproject.toml:
[tool.cibuildwheel]
before-test = ["python -m pip install replace-pip-with-uv-pip"]
```
