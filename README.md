# AQUA-friends-template

Template repository for an **AQUA-friend**.

## What is an AQUA-friend?

An AQUA-friend is a data analysis package that lives outside the official AQUA codebase
but is built to work *with* AQUA. It uses AQUA core (the `Reader` and
related utilities) as a library and can expose a command-line interface that
AQUA analysis can launch.

AQUA-friends are collected under the [AQUA-friends](https://github.com/AQUA-friends)
organisation. Each AQUA-friend is its own repository, with its own
install procedure, dependencies, and maintainer.

The only requirements for an AQUA-friend is to import [AQUA](https://github.com/DestinE-Climate-DT/AQUA) and to use the AQUA [reader](https://github.com/DestinE-Climate-DT/AQUA/blob/main/aqua/core/reader/reader.py).

## Repository layout

```
aqua-friends-template/
├── README.md
├── CONTRIBUTING.md
├── pyproject.toml
├── src/
└── notebooks/
```

## How to use this template

1. Click *Use this template* on GitHub (or fork it).
2. Rename the repository.
3. Replace this README with documentation of your own diagnostic, and
   adjust `pyproject.toml` (authors, dependencies, etc.).
4. Pick a license that suits your work and add a `LICENSE` file.
