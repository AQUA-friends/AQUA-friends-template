# AQUA-friends-template

Template repository for an **AQUA-friend**.

## What is an AQUA-friend?

An AQUA-friend is a data analysis package that lives outside the official AQUA codebase
but is built to work *with* AQUA. It uses AQUA core (the `Reader` and
related utilities) as a library, exposes a command-line interface that
AQUA analysis can launch, and otherwise stays independent.

AQUA-friends are collected under the [AQUA-friends](https://github.com/AQUA-friends)
organisation. Each AQUA-friend is its own repository, with its own
install procedure, dependencies, and maintainer.

## The three requirements every AQUA-friend must satisfy

1. **It exposes a CLI.** The CLI must accept the flags that `aqua analysis`
   passes to every diagnostic (see [CLI contract](#cli-contract) below), so
   that the AQUA-friend can be launched through the existing AQUA analysis
   pipeline alongside official diagnostics.
2. **It imports AQUA.** `import aqua` must work — i.e. the AQUA core library
   is a hard dependency.
3. **It uses AQUA functionality.** Typically this means using
   `aqua.core.reader.Reader` as the data entry point (catalog access,
   fixing, regridding, statistics) instead of reading files directly.

## Repository layout

```
aqua-friends-template/
├── README.md
├── CONTRIBUTING.md
├── pyproject.toml
├── aqua_friends_template/        <- the Python package (rename when you fork)
│   ├── __init__.py
│   └── file.py
├── cli/
│   └── cli_template.py           <- entry point for `aqua analysis`
└── config/
    └── config_template.yaml  <- example diagnostic config
```

## CLI contract

`aqua analysis` launches each tool roughly as:

```
python <cli_script> --model <M> --exp <E> --source <S> --outputdir <O> \
                   --config <cfg.yaml> -l <LOGLEVEL> [optional flags...]
```

The CLI of an AQUA-friend must accept **all** of the following flags
(gracefully ignoring those that are irrelevant to it):

| Flag | When it is passed |
|---|---|
| `--model`, `--exp`, `--source`, `--outputdir`, `--config`, `-l/--loglevel` | always |
| `--catalog` | if the user picked a catalog explicitly |
| `--realization` | if a realization was requested |
| `--startdate`, `--enddate` | if a time slice was requested |
| `--regrid` | if regridding was requested |
| `--nworkers`, `--nthreads` | when running with the parallel Dask backend |
| `--cluster` | address of the shared Dask scheduler (if used) |
| `--source_oce` | if the diagnostic declares `source_oce: true` in its analysis-config entry |

The stub in [`cli/cli_template.py`](cli/cli_template.py) already declares
every flag in argparse, so you only need to consume the ones you actually
use.

## Integrating an AQUA-friend with `aqua analysis`

In your `aqua-analysis` YAML config, register the AQUA-friend under
`cli:` (using an **absolute path** to the CLI script, since
`script_path_base` in the analysis YAML points at the AQUA-diagnostics
tree) and add a `diagnostics:` entry for it:

```yaml
cli:
  my_friend: "/abs/path/to/aqua-friend-mything/cli/cli_my_friend.py"

run:
    - ["my_collection"]

diagnostics:
  my_collection:
    my_friend:
      config: "/abs/path/to/my-friend-config.yaml"
```

After that, `aqua-analysis -c <your-config.yaml>` will launch the
AQUA-friend along with the rest of your run.

## How to use this template

1. Click *Use this template* on GitHub (or fork it).
2. Rename the repository, the `aqua_friends_template/` package and the
   example config to match your tool's name. (`cli/cli_template.py` can
   stay as is, or be renamed if you prefer.)
3. Fill in the `TODO`s in `aqua_friends_template/diagnostic.py`.
4. Replace this README with documentation of your own diagnostic, and
   adjust `pyproject.toml` (authors, dependencies, etc.).
5. Pick a license that suits your work and add a `LICENSE` file.
