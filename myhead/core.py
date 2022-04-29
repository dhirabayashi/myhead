import click
import sys

from myhead import printer


@click.command()
@click.option('--lines', '-n', 'line_count', default=10, show_default=True,
              help='Print count lines of each of the specified files.')
@click.option('--bytes', '-c', 'byte_count', type=int, help='Print bytes of each of the specified files.')
@click.argument('files', nargs=-1, required=False)
def cmd(files, line_count, byte_count):
    """headコマンドクローン"""
    __my_head(files, line_count, byte_count)


def __my_head(files, line_count, byte_count):
    if byte_count:
        __print_bytes(files, byte_count)
    else:
        __print_lines(files, line_count)


def __print_lines(files, line_count):
    if files:
        for file in files:
            printer.print_file_lines(file, line_count, len(files) != 1, sys.stdout)
    else:
        printer.print_stdin_lines(line_count, sys.stdin, sys.stdout)


def __print_bytes(files, byte_count):
    if files:
        for file in files:
            printer.print_file_bytes(file, byte_count, len(files) != 1, sys.stdout)
    else:
        printer.print_stdin_bytes(byte_count, sys.stdin, sys.stdout)
