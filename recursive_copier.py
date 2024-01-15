import argparse
import shutil
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="recursive_copier",
    description="Recursively copies files from one directory to another directory based on their file extension.",
)

parser.add_argument("-s", "--source", type=Path, required=True, help="Source directory")
parser.add_argument(
    "-d",
    "--destination",
    type=Path,
    required=False,
    default="dist",
    help="Destination directory (default: ./%(default)s)",
)


def recursive_copy(source: Path, destination: Path):
    """
    Recursively copies a file or directory from the source path to the destination path.

    Args:
        source (Path): The path of the file or directory to be copied.
        destination (Path): The path of the destination directory where the file or directory will be copied to.

    Returns:
        None
    """
    try:
        if source.is_file():
            file_extension = source.suffix.lower()

            destination_subdirectory = destination / file_extension[1:]
            destination_subdirectory.mkdir(parents=True, exist_ok=True)

            destination_file = destination_subdirectory / source.name
            print(f"Copying {source} to {destination_file}")
            shutil.copy2(source, destination_file, follow_symlinks=False)
        else:
            for file in source.iterdir():
                recursive_copy(file, destination)
    except OSError as e:
        print(f"Failed to copy {source} to {destination}: {e}")


if __name__ == "__main__":
    args = parser.parse_args()
    recursive_copy(args.source, args.destination)
