# Завдання 1

import shutil
import argparse
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--source", type=Path, required=True, help="Source directory"
    )
    parser.add_argument(
        "-d",
        "--destination",
        type=Path,
        default=Path("dist"),
        help="Destination directory",
    )
    return parser.parse_args()


def copy_files(source: Path, destination: Path):
    try:
        for item in source.iterdir():
            if item.is_dir():
                copy_files(item, destination)
            else:
                folder = destination / item.suffix[1:]
                try:
                    folder.mkdir(parents=True, exist_ok=True)
                except PermissionError:
                    print(f"Can't create {folder}, permission denied.")
                try:
                    shutil.copy(item, folder)
                except PermissionError:
                    print(f"Can't copy {item}, permission denied.")
                except shutil.SameFileError:
                    pass
    except FileNotFoundError:
        print(f"Can't find directory {source}")
    except NotADirectoryError:
        print(f"{source} is not a directory.")
    except PermissionError:
        print(f"Can't read {source}, permission denied.")


def main():
    args = parse_args()
    copy_files(args.source, args.destination)


if __name__ == "__main__":
    main()
