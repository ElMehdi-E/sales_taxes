![Tests](https://github.com/ElMehdi-E/sales_taxes/actions/workflows/tests.yml/badge.svg)

# sales_taxes

An application that prints out the receipt details, including sales taxes, for a given shopping basket.

## Requirements

- Python >=3.6

- Make sure you have the latest [pip](https://pip.pypa.io/en/stable/) version
```bash
pip install --upgrade pip
```

- Install the development requirements
```bash
pip install -r requirements_dev.txt 
```

## Installation

```bash
pip install -e .  # or "python setup.py develop"
```

## Run tests

```bash
pytest
```

Flake8 is a toolkit for checking the code against coding style (PEP8), programming errors (like “library imported but unused” and “Undefined name”)

```bash
flake8 src tests
```

## Credits
The configuration files are based on the [TestingStarterProject](https://github.com/mCodingLLC/SlapThatLikeButton-TestingStarterProject) project template.
