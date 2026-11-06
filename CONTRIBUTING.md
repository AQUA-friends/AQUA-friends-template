# Contributing

This file applies to people authoring a **new AQUA-friend** by forking
this template. If instead you want to suggest a change to the template
itself, open an issue or PR on the
[AQUA-friends-template](https://github.com/AQUA-friends/AQUA-friends-template)
repository.

## Starting a new AQUA-friend from this template

1. Use *Use this template* on GitHub to create a new repository under the
   [AQUA-friends](https://github.com/AQUA-friends) organisation.
2. Rename the `name` field in `pyproject.toml`
3. Update this `CONTRIBUTING.md` and the `README.md` to describe **your**
   AQUA-friend.
4. Modify the `LICENSE` file. By default we suggest the MIT license, but you can choose any other license that suits your needs. Make sure to update the copyright notice and the year.

5. Choose, among the options in the `README.md`, your environment files and your
   coherence level with AQUA. Delete the optional files you do not need, then state
   your choices in your own `README.md`.
6. Document every change in `CHANGELOG.md`, in the same format as AQUA and
   AQUA-diagnostics, citing the pull request number.

## Keeping your AQUA-friend compatible

Whatever you do inside your AQUA-friend, make sure that `import aqua` keeps 
being a hard dependency.
A pin of the AQUA version is possible, so that any update in the AQUA `main` 
branch does not break the compatibility of the tool.

## Suggesting changes to AQUA core

If during the development of your AQUA-friend you find that AQUA core is
missing a feature you need (e.g. a new interpolation method, support for
streamed processing of a specific data source, etc.), please open an issue
in the [AQUA](https://github.com/DestinE-Climate-DT/AQUA) repository
describing the use case rather than working around it locally — that is
the most useful kind of feedback for the core team.
