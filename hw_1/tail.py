import argparse
import sys
from io import TextIOWrapper


def process_stream(
        stream: TextIOWrapper,
        count: int,
        name: str | None = None,
        print_header: bool = False) -> None:
    """
    Read all lines from stream, then print the last `count` of them.

    :param stream: The stream to read
    :param count: The amount lines to read
    :param name: The name of the file if any
    :param print_header: Whether to print a header or not.
    """
    lines = stream.readlines()[-count:]
    if print_header and name:
        print(f"==> {name} <==")
    for line in lines:
        print(line, end='')


def main():
    """
    A simplified version of the Unix `tail` utility: print the last N lines of each given file.

    Usage:
        python tail.py [FILE ...]

    If one or more FILEs are provided, prints the last 10 lines of each. If multiple files,
    prints a header in the form "==> FILE_NAME <==" before each file's output.
    If no FILE is provided, reads from stdin and prints the last 17 lines.
    """
    parser = argparse.ArgumentParser(description="Simplified tail: print last lines of files or stdin.")
    parser.add_argument(
        'files',
        nargs='*',
        type=argparse.FileType(),
        default=[],
        help='Input files (default: stdin)'
    )
    args = parser.parse_args()
    if not args.files:
        process_stream(sys.stdin, 17)
        return
    multiple = len(args.files) > 1
    for idx, f in enumerate(args.files):
        if multiple:
            if idx > 0:
                print()
            process_stream(f, 10, name=f.name, print_header=True)
        else:
            process_stream(f, 10)


if __name__ == '__main__':
    main()
