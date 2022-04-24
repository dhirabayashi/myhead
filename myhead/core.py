import click

from myhead.printer import print_file, print_stdin


@click.command()
@click.argument('file', required=False)
@click.option('-n', default=10)
def cmd(file, n):
    """headコマンドクローン"""
    __print_lines(file, n)


def __print_lines(file, n):
    if file:
        print_file(file, n)
    else:
        print_stdin(n)
