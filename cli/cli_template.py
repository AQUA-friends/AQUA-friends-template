#!/usr/bin/env python3
"""CLI for the AQUA-friend template diagnostic.

This script is the entry point invoked by `aqua analysis`. Its argparse
interface accepts every flag that `aqua analysis` may pass — even those
this template ignores — so that the script remains drop-in compatible
with the AQUA analysis machinery.

Run it directly:

    python cli/cli_template.py \
        --model IFS-NEMO-5km --exp baseline-hist --source lra-r100-monthly \
        --outputdir ./output --config config/config_aqua_friends_template.yaml \
        -l INFO
"""

import argparse
import sys

from aqua.core.util import load_yaml

from aqua_friends_template import AquaFriendDiagnostic


def parse_args(argv=None):
    """Build the argparse parser and parse arguments.

    The full set of flags reflects what `aqua analysis` may pass; see
    aqua/core/analysis/analysis.py for the source of truth.

    Args:
        argv (list, optional): Argument list. Defaults to sys.argv[1:].

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="AQUA-friend template diagnostic.")

    # Always passed by `aqua analysis`.
    parser.add_argument("--model", required=True, help="Model name.")
    parser.add_argument("--exp", required=True, help="Experiment name.")
    parser.add_argument("--source", required=True, help="Source name.")
    parser.add_argument("--outputdir", required=True, help="Output directory.")
    parser.add_argument("-c", "--config", required=True, help="Path to the diagnostic config YAML.")
    parser.add_argument(
        "-l", "--loglevel",
        type=str.upper,
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="WARNING",
        help="Log level.",
    )

    # Conditionally passed by `aqua analysis`.
    parser.add_argument("--catalog", default=None, help="Catalog name.")
    parser.add_argument("--realization", default=None, help="Realization name.")
    parser.add_argument("--startdate", default=None, help="Start date (YYYY-MM-DD).")
    parser.add_argument("--enddate", default=None, help="End date (YYYY-MM-DD).")
    parser.add_argument("--regrid", default=None, help="Target grid identifier.")
    parser.add_argument("-n", "--nworkers", type=int, default=None, help="Dask local-cluster workers.")
    parser.add_argument("--nthreads", type=int, default=None, help="Dask local-cluster threads per worker.")
    parser.add_argument("--cluster", default=None, help="Address of an existing Dask scheduler.")
    parser.add_argument("--source_oce", default=None, help="Extra ocean source when atmosphere is the main source.")

    return parser.parse_args(argv)


def main(argv=None):
    """Entry point. Parses CLI args, loads the YAML config, runs the diagnostic."""
    args = parse_args(argv)

    config = load_yaml(args.config) if args.config else {}

    diagnostic = AquaFriendDiagnostic(
        model=args.model,
        exp=args.exp,
        source=args.source,
        outputdir=args.outputdir,
        catalog=args.catalog,
        realization=args.realization,
        startdate=args.startdate,
        enddate=args.enddate,
        regrid=args.regrid,
        config=config,
        loglevel=args.loglevel,
    )
    diagnostic.run()


if __name__ == "__main__":
    main(sys.argv[1:])
