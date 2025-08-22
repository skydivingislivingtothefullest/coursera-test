#!/usr/bin/env python3
"""Display duplicate images identified by imagededup.

This script scans a directory for duplicate images using imagededup's
perceptual hashing (PHash) method and then visualizes each set of duplicates.

Example
-------
    python show_duplicates.py --dir /path/to/images
"""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Find and display duplicate images in a directory."
    )
    parser.add_argument(
        "--dir",
        type=Path,
        required=True,
        help="Path to the directory containing images to scan for duplicates.",
    )
    return parser.parse_args()


def main() -> None:
    """Execute the CLI to find and display duplicate images."""
    args = parse_args()

    if not args.dir.is_dir():
        raise SystemExit(f"Directory not found: {args.dir}")

    try:
        from imagededup.methods import PHash
        from imagededup.utils import plot_duplicates
    except ModuleNotFoundError as exc:  # pragma: no cover - depends on optional pkg
        raise SystemExit(
            "imagededup is required for this script. Install with 'pip install "
            "imagededup[full]'"
        ) from exc

    hasher = PHash()
    duplicates = hasher.find_duplicates(image_dir=str(args.dir))

    visited: set[str] = set()
    found_any = False
    for filename, dup_files in duplicates.items():
        if filename in visited:
            continue
        if dup_files:
            found_any = True
            plot_duplicates(
                image_dir=str(args.dir), duplicate_map=duplicates, filename=filename
            )
            visited.update(dup_files)
            visited.add(filename)

    if not found_any:
        print("No duplicates found.")


if __name__ == "__main__":
    main()
