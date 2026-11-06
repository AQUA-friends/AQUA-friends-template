# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)

## [Unreleased]
Unreleased in the current development version (target vX.Y.Z):

Main changes:

Complete list:
- Agents: `AGENTS.md` entry point reading AQUA's shared `AGENTS.common.md` from GitHub, `CLAUDE.md`, and the `new-aqua-friend` skill reusing the AQUA-diagnostics skill; levels and environment files are options to ask the user about (#6)
- Packaging: find the packages in `src/` (`where = ["src"]`), so that `src/<package>` is imported as `<package>` and not as `src.<package>` (#6)
