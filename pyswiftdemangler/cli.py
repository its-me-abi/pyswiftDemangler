"""Command-line interface for pyswiftdemangler."""

import argparse
import sys
from .core import demangler


def test():
    """Run built-in test with hardcoded value."""
    name = "_TtuRxs8RunciblerFxWx5Mince6Quince_"
    expected_value = "<A where A: Swift.Runcible>(A) -> A.Mince.Quince"

    try:
        result = demangler().get_demangled_name(name)
    except OSError as e:
        print(f"Error: Failed to load Swift DLL. {e}", file=sys.stderr)
        sys.exit(1)

    if result:
        print("Demangled successfully. Verifying...")
        print(f"   Input:    {name}")
        print(f"   Expected: {expected_value}")
        print(f"   Got:      {result}")

        if result == expected_value:
            print("\n✓ Verification successful!")
            return 0
        else:
            print("\n✗ Verification failed. Output does not match expected value.")
            return 1
    else:
        print(
            f"Error: Failed to demangle symbol. "
            f"Check if this is a valid Swift mangled symbol: {name}",
            file=sys.stderr,
        )
        return 1


def get_commandline_args():
    """Parse and return command-line arguments.
    
    Returns:
        tuple: (args, parser) from argparse.
    """
    parser = argparse.ArgumentParser(
        description="Demangle Swift symbol names using the official Swift DLL.",
        prog="pyswiftdemangler",
    )
    parser.add_argument(
        "-n",
        "--name",
        help="Mangled Swift symbol to demangle",
        type=str,
    )
    parser.add_argument(
        "-t",
        "--test",
        action="store_true",
        help="Run built-in test with hardcoded value",
    )
    args = parser.parse_args()
    return args, parser


def main():
    """Main entry point for the CLI."""
    args, parser = get_commandline_args()

    if args.name:
        try:
            d = demangler()
            result = d.get_demangled_name(args.name)
        except OSError as e:
            print(
                f"Error: Failed to load Swift DLL. {e}",
                file=sys.stderr,
            )
            sys.exit(1)

        if result:
            print(result)
            sys.exit(0)
        else:
            print(
                f"Error: Failed to demangle symbol. "
                f"Check if this is a valid Swift mangled symbol.",
                file=sys.stderr,
            )
            sys.exit(1)
    elif args.test:
        sys.exit(test())
    else:
        parser.print_help()
        sys.exit(0)


if __name__ == "__main__":
    main()
