# AQUA-friend Agent Instructions

Before starting work, retrieve and read both files in full, in this order:

1. Shared rules, directly from GitHub:
   [AQUA/AGENTS.common.md](https://raw.githubusercontent.com/DestinE-Climate-DT/AQUA/main/AGENTS.common.md).
2. This file.

Do not keep a local copy of `AGENTS.common.md` and do not load AQUA's `AGENTS.repo.md`.
If the shared rules cannot be retrieved or either file cannot be read in full,
report the problem and stop before making changes.

Never push directly to `main`. Merge a pull request only with the explicit human
authorization for that specific merge described in the shared rules.

## What applies, and what is only a suggestion

An AQUA-friend is not part of AQUA: it may analyse a specific topic with a pipeline that
differs a lot from the AQUA-diagnostics examples.

- **Always** (a hard requirement of every AQUA-friend): `import aqua` stays a hard dependency
  and data is read through the AQUA `Reader`. The process rules of `AGENTS.common.md`
  also always apply: human control of `main`, how to open issues and pull requests (title
  prefix, signature), and a `CHANGELOG.md` entry citing the pull request number.
- **Suggested**: the architecture and coding rules of `AGENTS.common.md`, the AQUA-diagnostics
  standards, the environment files and the coherence level (see the `README.md`).
  They are options the user picks from, not a checklist to complete.

Hence:

- Ask the user which coherence level (0, 1a, 1b, 2, 3) and which environment option
  they want, unless they already said. Do not decide in silence. Ask when the first code is
  about to be written: an assessment (see below) needs no choice yet, and until then the optional
  files stay untouched.
- Never create or fill an optional file (`requirements.txt`, `environment.yml`) that the user
  did not choose, and delete the optional templates they do not need.
- Apply the rules of the chosen level only. Do not add AQUA-diagnostics structures
  (base classes, CLI, config files) to an AQUA-friend that chose a lower level.
- Record the chosen level and environment in the `README.md`.

## Writing code at levels 2 and 3

Use the `new-aqua-friend` skill ([`.claude/skills/new-aqua-friend/SKILL.md`](.claude/skills/new-aqua-friend/SKILL.md));
agents that do not load skills read that file directly. The code of an AQUA-friend lives in `src/<package>/`.

## Wrapping an existing tool

When the AQUA-friend is meant to run a tool that already exists (written for another framework or for CMIP files),
do not rewrite it. Assess first, then code:

1. Write an `ASSESSMENT.md` before any integration code: what the tool needs as input, which of those variables the AQUA
   `Reader` can deliver (probe with one day of data before asking for a month), what can or cannot run, the
   environment conflicts, and a task list with the gates that decide whether to continue and a short verdict on the effort.
2. Prefer an adaptor: read with the `Reader`, regrid with AQUA if the tool needs a regular grid, and stage the data in the
   format the tool expects. Do not fork or vendor the tool, and check its licence.
3. Consume the tool as a pinned external checkout and drive it through its command line. If its pinned dependencies
   conflict with AQUA (Python, numpy, xarray), prefer two environments over patching the tool.
4. Anything missing from AQUA or from the data (variables, grids, runs) goes to the AQUA or catalog maintainers as an issue.

## Reading Climate DT data away from HPC

`Reader(..., engine="polytope")` reads from the data bridge with the credentials of `~/.polytopeapirc` (never read or print it).
The grid files of `aqua-dvc` are `.dvc` pointers until pulled: use `areas=False` for retrieval only, and ask the user before a
`dvc pull`, which is a download. Only some runs are on the bridge, so probe one day first.

## If this AQUA-friend is included in AQUA-diagnostics

Read the [AGENTS.md of AQUA-diagnostics](https://raw.githubusercontent.com/DestinE-Climate-DT/AQUA-diagnostics/main/AGENTS.md)
(and what it points to) to understand where each piece goes: it is the authority on that repository's layout, tests,
documentation and configuration. A skill for this step is proposed in
[AQUA-diagnostics#567](https://github.com/DestinE-Climate-DT/AQUA-diagnostics/issues/567).
