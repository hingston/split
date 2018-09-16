"""Split a file by n number of lines.

Created by William Hingston on 14/09/2018.

See:
    $ python split.py -h
"""

import argparse
import glob
import os
import tempfile
from itertools import zip_longest


# collect data into fixed length chunks or blocks
def grouper(n, iterable, fillvalue=None):
    a = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *a)


def split(n: int, path: str, file: str, suffix: str = None, encoding: str = "utf8"):
    filename, file_extension = os.path.splitext(file)

    if suffix is None:
        suffix = filename + "_part"
    else:
        suffix = filename + "_" + suffix

    for filename in glob.glob(path + suffix + "*"):
        os.remove(filename)

    count = 1

    with open(path + file, encoding=encoding) as f:
        for i, g in enumerate(grouper(n, f, fillvalue=None)):
            with tempfile.NamedTemporaryFile('w', encoding=encoding, delete=False) as fout:
                for j, line in enumerate(g, 1):  # count number of lines in group
                    if line is None:
                        j -= 1  # don't count this line
                        break
                    fout.write(line)
            os.rename(fout.name, '{0}{1}_{2}{3}'.format(path, suffix, count, file_extension))
            count += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser("$ python split.py", description="split files by number of lines")
    parser.add_argument("n", type=int, help="max number of lines per file")
    parser.add_argument("path", type=str, help="path of file")
    parser.add_argument("file", type=str, help="name of file to split")
    parser.add_argument("-s", "--suffix", type=str, help="suffix, default='part'", default=None)
    parser.add_argument("-e", "--encoding", type=str, help="encoding, default='utf8'", default="utf8")
    args = parser.parse_args()
    split(args.n, args.path, args.file, args.suffix, args.encoding)
