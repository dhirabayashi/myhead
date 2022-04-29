import tempfile
import textwrap
import unittest
from unittest.mock import Mock

from myhead import printer


class PrinterTest(unittest.TestCase):
    def test_print_file_lines(self):
        with tempfile.NamedTemporaryFile() as fp:
            # 準備
            text = """
            aaa
            bbb
            ccc
            """
            text = textwrap.dedent(text).strip()

            fp.write(text.encode())
            fp.flush()

            # モック
            stdout_mock = Mock()

            # 実行
            printer.print_file_lines(fp.name, 2, False, stdout_mock)

            # 検証
            self.assertEqual(2, stdout_mock.write.call_count)
            stdout_mock.write.assert_any_call('aaa\n')
            stdout_mock.write.assert_any_call('bbb\n')

    def test_print_file_bytes(self):
        with tempfile.NamedTemporaryFile() as fp:
            # 準備
            text = """
            aaa
            bbb
            ccc
            """
            text = textwrap.dedent(text).strip()

            fp.write(text.encode())
            fp.flush()

            # モック
            stdout_mock = Mock()

            # 実行
            printer.print_file_bytes(fp.name, 5, False, stdout_mock)

            # 検証
            self.assertEqual(2, stdout_mock.write.call_count)
            stdout_mock.write.assert_any_call('aaa\n')
            stdout_mock.write.assert_any_call('b')

    def test_print_stdin_lines(self):
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
        # モック
        stdin_mock = Mock()
        stdin_mock.readline.return_value = 'aaa\n'
        stdout_mock = Mock()

        # 実行
        printer.print_stdin_bytes(5, stdin_mock, stdout_mock)

        # 検証
        self.assertEqual(1, stdout_mock.write.call_count)
        stdout_mock.write.assert_any_call('aaa\na')
