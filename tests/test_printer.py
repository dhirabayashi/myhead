import tempfile
import textwrap
import unittest
from unittest.mock import Mock

from myhead import printer


class PrinterTest(unittest.TestCase):
    def setUp(self):
        fp = tempfile.NamedTemporaryFile()
        text = """
        aaa
        bbb
        ccc
        """
        text = textwrap.dedent(text).strip()

        fp.write(text.encode())
        fp.flush()

        self.fp = fp

    def tearDown(self):
        self.fp.close()

    def test_print_file_lines(self):
        """
        ファイル名入力（行数指定）の基本ケース
        """

        # モック
        stdout_mock = Mock()

        # 実行
        printer.print_file_lines(self.fp.name, 2, True, stdout_mock)

        # 検証
        self.assertEqual(3, stdout_mock.write.call_count)
        stdout_mock.write.assert_any_call(f'==> {self.fp.name} <==\n')
        stdout_mock.write.assert_any_call('aaa\n')
        stdout_mock.write.assert_any_call('bbb\n')

    def test_print_file_bytes(self):
        """
        ファイル名入力（バイト数指定）の基本ケース
        """

        # モック
        stdout_mock = Mock()

        # 実行
        printer.print_file_bytes(self.fp.name, 5, True, stdout_mock)

        # 検証
        self.assertEqual(3, stdout_mock.write.call_count)
        stdout_mock.write.assert_any_call(f'==> {self.fp.name} <==\n')
        stdout_mock.write.assert_any_call('aaa\n')
        stdout_mock.write.assert_any_call('b')

    def test_print_stdin_lines(self):
        """
        直接入力（行数指定）の基本ケース
        """

        # モック
        stdin_mock = Mock()
        stdin_mock.readline.return_value = 'aaa\n'
        stdout_mock = Mock()

        # 実行
        printer.print_stdin_lines(2, stdin_mock, stdout_mock)

        # 検証
        self.assertEqual(2, stdout_mock.write.call_count)
        stdout_mock.write.assert_any_call('aaa\n')
        stdout_mock.write.assert_any_call('aaa\n')

    def test_print_stdin_bytes(self):
        """
        直接入力（バイト数指定）の基本ケース
        """

        # モック
        stdin_mock = Mock()
        stdin_mock.readline.return_value = 'aaa\n'
        stdout_mock = Mock()

        # 実行
        printer.print_stdin_bytes(5, stdin_mock, stdout_mock)

        # 検証
        self.assertEqual(1, stdout_mock.write.call_count)
        stdout_mock.write.assert_any_call('aaa\na')
