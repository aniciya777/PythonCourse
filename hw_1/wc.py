import argparse
import sys


class Count:
    """
    Stores number of lines, words, and bytes.
    """
    __slots__ = ['_lines', '_words', '_bytes', '_name']
    _total_lines = 0
    _total_words = 0
    _total_bytes = 0

    @classmethod
    def clear(cls):
        cls._total_lines = 0
        cls._total_words = 0
        cls._total_bytes = 0

    def __init__(self, text: bytes = bytes(), name: str | None = None):
        self._lines = text.count(b'\n')
        self._words = len(text.split())
        self._bytes = len(text)
        self._name = name
        self.__class__._total_lines += self._lines
        self.__class__._total_words += self._words
        self.__class__._total_bytes += self._bytes

    @classmethod
    def get_total(cls) -> 'Count':
        result = cls(name='total')
        result._lines = cls._total_lines
        result._words = cls._total_words
        result._bytes = cls._total_bytes
        return result

    def __str__(self) -> str:
        if self._name is None:
            width = max(7, len(str(self.__class__._total_bytes)))
        else:
            width = max(3, len(str(self.__class__._total_bytes)))
        str_lines = str(self._lines).rjust(width)
        str_words = str(self._words).rjust(width)
        str_bytes = str(self._bytes).rjust(width)
        if self._name is not None:
            return f'{str_lines} {str_words} {str_bytes} {self._name}'
        return f'{str_lines} {str_words} {str_bytes}'


def main():
    """
    Simplified version of Unix `wc` utility without options: count lines, words, and bytes.

    Usage:
        python wc.py [FILE ...]

    If one or more FILEs are provided, prints counts and file names. If multiple files are given,
    adds a final line with totals. If no FILE is provided, reads from stdin and prints counts only.
    """
    parser = argparse.ArgumentParser(description="Simplified wc: count lines, words, and bytes.")
    parser.add_argument(
        'files',
        nargs='*',
        type=argparse.FileType('rb'),
        help='Input files (default: stdin)'
    )
    args = parser.parse_args()
    Count.clear()
    if not args.files:
        text = sys.stdin.buffer.read()
        print(Count(text))
        return
    multiple = len(args.files) > 1
    counts = []
    for f in args.files:
        try:
            data = f.read()
        except Exception as e:
            print(f"wc.py: {f.name}: {e}", file=sys.stderr)
            continue
        counts.append(Count(data, f.name))
        f.close()
    for c in counts:
        print(c)
    if multiple:
        print(Count.get_total())


if __name__ == '__main__':
    main()
