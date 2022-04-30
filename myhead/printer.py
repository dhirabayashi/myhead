import os.path
import sys


def print_file_lines(file, line_count, show_header, out):
    """ファイルの内容を指定行数のみ出力する

    :param file: 対象のファイルパス
    :param line_count: 表示する行数
    :param show_header: ファイル名を表示するかどうか
    :param out: 出力先
    :return: None
    """

    # ファイルのチェック
    if msg := __generate_error_message(file):
        print(f'myhead: {msg}', file=sys.stderr)
        return 1

    # ファイル名の出力
    if show_header:
        out.write(f'==> {file} <==\n')

    current_count = 0
    # ファイル入力
    with open(file) as f:
        # 指定行数分だけ出力する
        for line in f:
            if current_count == line_count:
                break

            # 改行コードは置き換える
            line = line.rstrip() + '\n'
            out.write(line)
            current_count += 1

    return 0


def print_file_bytes(file, byte_count, show_header, out):
    """ファイルの内容を指定バイト数のみ出力する

    :param file: 対象のファイルパス
    :param byte_count: 表示する行数
    :param show_header: ファイル名を表示するかどうか
    :param out: 出力先
    :return: None
    """

    # ファイルのチェック
    if msg := __generate_error_message(file):
        print(f'myhead: {msg}', file=sys.stderr)
        return 1

    # ファイル名の出力
    if show_header:
        out.write(f'==> {file} <==\n')

    remaining_byte_count = byte_count
    # ファイル入力
    with open(file) as f:
        # 行単位で読み込み、バイト数に達するかEOFに到達するまで表示する
        for line in f:
            encoded_line = line.encode()

            # 残りバイト数
            remaining_byte_count -= len(encoded_line)

            if remaining_byte_count >= 0:
                output = line
            else:
                rest = abs(remaining_byte_count)
                output = encoded_line[:len(encoded_line) - rest].decode()

            out.write(output)

            if remaining_byte_count <= 0:
                break

    return 0


def print_stdin_lines(line_count, stdin, out):
    """標準入力に指定行数分入力させて出力する

    :param line_count: 表示する行数
    :param stdin: 標準入力
    :param out: 出力先
    :return: None
    """
    for _ in range(line_count):
        line = stdin.readline()
        out.write(line)


def print_stdin_bytes(byte_count, stdin, out):
    """標準入力入力させて、指定バイト数分だけ出力する

    :param byte_count: 表示するバイト数
    :param stdin: 標準入力
    :param out: 出力先
    :return: None
    """

    # 行単位で入力させ、バイト数に達するかEOFが入力されるまで入力
    inputs = ''
    while line := stdin.readline():
        inputs += line

        if len(inputs) >= byte_count:
            break

    # バイト数分切り取って表示
    output = inputs.encode()[:byte_count].decode(errors='replace')
    out.write(output)


def __generate_error_message(filename):
    if not os.path.exists(filename):
        return f'{filename}: No such file or directory'

    if os.path.isdir(filename):
        return f'Error reading {filename}'

    if not os.access(filename, os.R_OK):
        return f'{filename}: Permission denied'

    return None
