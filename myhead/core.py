import click
import sys


@click.command()
@click.argument('file', required=False)
def cmd(file):
    if file:
        with open(file) as f:
            for line in f:
                print(line)
    else:
        while line := sys.stdin.readline():
            print(line, end='')


if __name__ == '__main__':
    cmd()
