---
name: new-aqua-friend
description: Add analysis code to an AQUA-friend following AQUA conventions at the level the user chooses (coherence levels 0 to 3 in the README). For levels 2 and 3 it reuses the new-aqua-diagnostic skill of AQUA-diagnostics, fetched from GitHub, with src/<package>/ as target instead of aqua/diagnostics/. Use when the user wants to add a compute class, plot class, CLI or config to this repository, or asks how to structure it.
---

# Writing code in an AQUA-friend

An AQUA-friend follows AQUA only as far as its author chooses. The levels are **suggestions, not requirements**
(see `README.md` and `AGENTS.md`). This skill adds no standards of its own: it points to the AQUA ones and
says how to adapt them to this repository. Nothing is copied here, so there is nothing to keep in sync.

## 1. Settle the level first

Ask the user, in one message and with your proposed default, unless the request already answers:

| Choice | Default to propose |
|---|---|
| Coherence level: 0 Reader only, 1a core methods, 1b core plots, 2 AQUA-diagnostics classes, 3 CLI and config standards | the lowest level that does the job |
| Package name under `src/` | the repository name in snake_case |
| What it computes (quantity, variables, regions, period, figure) | no default, ask |
| Environment option and optional files (see `README.md`) | `pyproject.toml` only |

Do not do more than the chosen level. Do not create the optional env files unless the user picked them.

## 2. Levels 0, 1a, 1b

No skeleton. Use the `Reader` and the reuse map in
[AGENTS.common.md](https://raw.githubusercontent.com/DestinE-Climate-DT/AQUA/main/AGENTS.common.md).
For 1a use the core operators of the `Reader` (`regrid`, `fldmean`, `timmean`, ...) instead of reimplementing them.
For 1b draw with `aqua.core.graphics`. Anything missing in core: open an issue on AQUA (see `CONTRIBUTING.md`).

## 3. Levels 2 and 3: reuse the AQUA-diagnostics skill

Fetch the upstream skill into a folder **outside** this repository, then read `SKILL.md` and `reference.md` there
in full, plus `AGENTS.repo.md` and `DIAGNOSTIC_GUIDELINES.md`. Read `scripts/instantiate.sh` before running it.

```bash
UP=$(mktemp -d)
git clone --depth 1 --filter=blob:none --sparse https://github.com/DestinE-Climate-DT/AQUA-diagnostics.git "$UP"
git -C "$UP" sparse-checkout set .claude/skills/new-aqua-diagnostic
```

Follow the upstream procedure (open choices, tool, three layers, tests), where the code disagrees with the docs
follow the code, and apply this mapping:

| Upstream | In this repository |
|---|---|
| `aqua/diagnostics/<name>/` | `src/<package>/<name>/`; imports `aqua.diagnostics.<name>` become `<package>.<name>`. `aqua.core.*` and `aqua.diagnostics.base` stay |
| Skeleton: `instantiate.sh <name> [Class] <scratch-dir>` | run it with a scratch dir as 3rd argument, then move the files below and replace the imports; never write it into this repository directly |
| `templates/collections/config-<name>.yaml` | `config/config-<name>.yaml`; the CLI default config lookup does not resolve here, run with `--config` |
| `tests/<name>/`, `tests/cli/` | `tests/`; replace `tests.shared_constants` with constants copied from the upstream file (only those used); the `ci` catalog exists only where the AQUA `ci` catalog is installed, otherwise use data you have |
| `.rst` page, `docs/sphinx` | skip, document in `README.md` |
| Level 2 only | drop `cli_<name>.py`, the config template and their tests |
| `aqua analysis` wiring, `config.grouping.yaml`, `KNOWN_DIAGNOSTIC_KEYS`, collections | skip: they belong to AQUA-diagnostics (see `AGENTS.md`, last section) |
| CHANGELOG entry | this repository's `CHANGELOG.md`, citing the pull request number |

Add the packages the code imports to `pyproject.toml` (`aqua-diagnostics[core]` instead of `aqua-core`), and to the
optional env files only if the user chose them. Run `ruff check` and the tests of what you added.
