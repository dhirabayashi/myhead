def print_file(file, n, show_header, out):
    """ファイルの内容を指定行数のみ出力する

    :param file: 対象のファイルパス
    :param n: 行数
    :param show_header: ファイル名を表示するかどうか
    :param out: 出力先
    :return: None
    """
    if show_header:
        out.write(f'==> {file} <==\n')

    try:
        count = 0
        # ファイル入力
        with open(file) as f:
            # 指定行数分だけ出力する
            for line in f:
                if count == n:
                    break

                # 改行コードは置き換える
                line = line.rstrip() + '\n'
                out.write(line)
                count += 1
    finally:
        out.flush()


def print_stdin(n, stdin, out):
    """標準入力に指定行数分入力させて出力する

    :param n: 入力、表示行数
    :param stdin: 標準入力
    :param out: 出力先
    :return: None
    """
    for _ in range(n):
        line = stdin.readline()
        out.write(line)
