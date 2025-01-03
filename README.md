# re-static-mypy
![Static Badge](https://img.shields.io/badge/Python-3.9_%7C_3.10_%7C_3.11_%7C_3.12_%7C_3.13-blue?logo=python&logoColor=white)
[![Stable Version](https://img.shields.io/pypi/v/re-static-mypy?color=blue)](https://pypi.org/project/re-static-mypy/)
[![stability-beta](https://img.shields.io/badge/stability-beta-33bbff.svg)](https://github.com/mkenney/software-guides/blob/master/STABILITY-BADGES.md#beta)

[![Python tests](https://github.com/mingaleg/re-static-mypy/actions/workflows/python-tests.yml/badge.svg?branch=main)](https://github.com/mingaleg/re-static-mypy/actions/workflows/python-tests.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/593e78ec96ed5ebb0dd3/maintainability)](https://codeclimate.com/github/mingaleg/re-static-mypy/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/593e78ec96ed5ebb0dd3/test_coverage)](https://codeclimate.com/github/mingaleg/re-static-mypy/test_coverage)

[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)


## Package release

This setup uses [poetry-dynamic-versioning](https://github.com/mtkennerly/poetry-dynamic-versioning).
This means it's not necessary to commit the version in the code but the CI pipeline
will infer it from the git tag.

To release a new version, just create a new release and tag in the GitHub repository, to:

* Build and deploy the python package to PyPI
* Build and deploy a new version of the documentation to GitHub pages

**IMPORTANT:** The default configuration requires the release name and the tag to follow
the convention `vX.X.X` (semantic versioning preceded by lowercase `v`). It will publish
the correct version on Pypi, omitting the `v` (ie. `v1.0.0` will publish `1.0.0`).

This format can be customized, refer to [poetry-dynamic-versioning docs](https://github.com/mtkennerly/poetry-dynamic-versioning)

## Commands for development

All the common commands used during development can be run using make targets:

* `make dev-dependencies`: Install dev requirements
* `make update-dependencies`: Update dev requirements
* `make fix`: Run code style and lint automatic fixes (where possible)
* `make test`: Run test suite against system python version
* `make check`: Run tests against all available python versions, code style and lint checks
* `make type`, `make format`, `make lint`, `make bandit`: Run the relevant check
* `make docs`: Render the mkdocs website locally
