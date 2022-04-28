import click
import sys

from myhead.printer import print_file, print_stdin


@click.command()
@click.option('--line', '-n', default=10, show_default=True, help='Print count lines of each of the specified files.')
@click.argument('files', nargs=-1, required=False)
def cmd(files, line):
    """headコマンドクローン"""
    __print_lines(files, line)


def __print_lines(files, n):
    if files:
        for file in files:
            print_file(file, n, len(files) != 1, sys.stdout)
    else:
        print_stdin(n, sys.stdin, sys.stdout)
