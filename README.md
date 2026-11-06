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
├── CHANGELOG.md
├── AGENTS.md          (instructions for AI agents, CLAUDE.md points to it)
├── .claude/skills/    (skill to write code at coherence levels 2 and 3)
├── pyproject.toml
├── requirements.txt   (optional)
├── environment.yml    (optional)
├── src/
└── notebooks/
```

## Environment: pick one

Everything below is an **option, not a checklist**. Choose what your AQUA-friend needs, delete the
rest, and do not fill in files you do not use.

1. **`pyproject.toml` only** (default). Enough when `pip install .` brings all you need.
2. **Add `requirements.txt`** if you need extra pip packages or pins on top of `pyproject.toml`.
3. **Add `environment.yml`** if you need conda packages, or extra binaries required by AQUA core.
   The template builds on the conda-forge `aqua-core` and installs `aqua-diagnostics` with pip.
4. **No environment file at all**, stating in your README that the AQUA-friend runs in the same
   environment as [AQUA-diagnostics](https://github.com/DestinE-Climate-DT/AQUA-diagnostics),
   if it needs nothing more.

## Coherence with AQUA: choose your level

How closely an AQUA-friend follows AQUA is up to you. The levels are **suggestions, not requirements**:
AQUA-friends may analyse specific topics with pipelines that differ a lot from the examples in
AQUA-diagnostics, so adopt what is useful and skip the rest. The levels are cumulative.

| Level | What it means |
|---|---|
| 0 | AQUA `Reader` only, no other core or diagnostics tool. |
| 1a | Also use AQUA core methods (`regrid`, `fldmean`, ...), see the [AQUA documentation](https://github.com/DestinE-Climate-DT/AQUA) or its `AGENTS.md`. |
| 1b | Also use the AQUA core plotting routines, or a similar style. |
| 2 | Also use AQUA-diagnostics: a class for the NetCDF production derived from the `Diagnostic` base class, and a class for the plots. |
| 3 | Also adopt the AQUA CLI and configuration file standards. |

The AQUA-diagnostics documentation and its `AGENTS.md` describe the current standards for levels 2 and 3.

## How to use this template

1. Click *Use this template* on GitHub (or fork it).
2. Rename the repository.
3. Replace this README with documentation of your own diagnostic, and
   adjust `pyproject.toml` (authors, dependencies, etc.).
4. Pick a license that suits your work and add a `LICENSE` file.
