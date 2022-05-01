import click
import sys

from myhead import printer


@click.command()
@click.option('--lines', '-n', 'line_count', type=int, show_default=True,
              help='Print count lines of each of the specified files.')
@click.option('--bytes', '-c', 'byte_count', type=int, help='Print bytes of each of the specified files.')
@click.argument('files', nargs=-1, required=False)
def cmd(files, line_count, byte_count):
    """
    headコマンドクローンのエントリポイント
    :param files: ファイル名
    :param line_count: 表示行数
    :param byte_count: 表示バイト数
    """

    # バリデーション
    if line_count and line_count < 1:
        print(f'myhead: illegal line count -- {line_count}', file=sys.stderr)
        sys.exit(1)

    if byte_count and byte_count < 1:
        print(f'myhead: illegal byte count -- {byte_count}', file=sys.stderr)
        sys.exit(1)

    if byte_count and line_count:
        print(f"myhead: can't combine line and byte counts")
        sys.exit(1)

    # デフォルト値
    if (not line_count) and (not byte_count):
        line_count = 10

    # ファイルは存在するものとしないものが混在するかもしれず、存在するものは表示するため後でチェックする
    ret = __my_head(files, line_count, byte_count)
    sys.exit(ret)


def __my_head(files, line_count, byte_count):
    """
    headコマンド本体処理
    :param files: ファイル名
    :param line_count: 表示行数
    :param byte_count: 表示バイト数
    :return: 終了コード
    """

    # 表示に使用する関数、値を設定
    if byte_count:
        print_file = printer.print_file_bytes
        print_stdin = printer.print_stdin_bytes
        count = byte_count
    else:
        print_file = printer.print_file_lines
        print_stdin = printer.print_stdin_lines
        count = line_count

    # 実行
    whole_ret = 0
    if files:
        for file in files:
            ret = print_file(file, count, len(files) != 1, sys.stdout)
            if ret:
                whole_ret = ret
    else:
        print_stdin(count, sys.stdin, sys.stdout)

    return whole_ret
