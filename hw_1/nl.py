import sys
import argparse


def main():
    """
    A simplified version of the Unix `nl -b a` utility: number all lines (including blank ones) from a file or stdin.

    Usage:
        python3 nl.py [FILE]

    If FILE is not provided, reads from standard input.
    """
    parser = argparse.ArgumentParser(description="Simplified nl -b a: number all lines, including blank ones.")
    parser.add_argument(
        'file',
        nargs='?',
        type=argparse.FileType(),
        default=sys.stdin,
        help='Input file (default: stdin)'
    )
    args = parser.parse_args()
    for i, line in enumerate(args.file, 1):
        text = line.rstrip('\n')
        print(f"{i:>6}\t{text}")
    if args.file is not sys.stdin:
        args.file.close()


if __name__ == '__main__':
    main()
