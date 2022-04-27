import tempfile
import textwrap
import unittest
from unittest.mock import Mock

from myhead.printer import print_file, print_stdin


class PrinterTest(unittest.TestCase):
    def test_print_file(self):
        with tempfile.NamedTemporaryFile() as fp:
            # 準備
            text = """
            aaa
            bbb
            ccc
            """
            text = textwrap.dedent(text).strip()

            fp.write(text.encode('utf-8'))
            fp.flush()

            # モック
            stdout_mock = Mock()

            # 実行
            print_file(fp.name, 2, stdout_mock)

            # 検証
            self.assertEqual(2, stdout_mock.write.call_count)
            stdout_mock.write.assert_any_call('aaa\n')
            stdout_mock.write.assert_any_call('bbb\n')
            stdout_mock.flush.assert_called_once()

    def test_print_stdin(self):
        # モック
        stdin_mock = Mock()
        stdin_mock.readline.return_value = 'aaa\n'
        stdout_mock = Mock()

        # 実行
        print_stdin(2, stdin_mock, stdout_mock)

        # 検証
        self.assertEqual(2, stdout_mock.write.call_count)
        stdout_mock.write.assert_any_call('aaa\n')
        stdout_mock.write.assert_any_call('aaa\n')
