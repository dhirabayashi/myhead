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

    # バリデーション
    if line_count and line_count < 1:
        print(f'myhead: illegal line count -- {line_count}', file=sys.stderr)
        sys.exit(1)

    if byte_count and byte_count < 1:
        print(f'myhead: illegal byte count -- {byte_count}', file=sys.stderr)
        sys.exit(1)

    # ファイルは存在するものとしないものが混在するかもしれず、存在するものは表示するため後でチェックする
    ret = __my_head(files, line_count, byte_count)
    sys.exit(ret)


def __my_head(files, line_count, byte_count):
    if byte_count:
        ret = __print_bytes(files, byte_count)
    else:
        ret = __print_lines(files, line_count)
    return ret


def __print_lines(files, line_count):
    whole_ret = 0
    if files:
        for file in files:
            ret = printer.print_file_lines(file, line_count, len(files) != 1, sys.stdout)
            if ret:
                whole_ret = ret
    else:
        printer.print_stdin_lines(line_count, sys.stdin, sys.stdout)

    return whole_ret


def __print_bytes(files, byte_count):
    whole_ret = 0
    if files:
        for file in files:
            ret = printer.print_file_bytes(file, byte_count, len(files) != 1, sys.stdout)
            if ret:
                whole_ret = ret
    else:
        printer.print_stdin_bytes(byte_count, sys.stdin, sys.stdout)

    return whole_ret
