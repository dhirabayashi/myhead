import textwrap
import unittest
import tempfile
from test.support import captured_stdout

from myhead.printer import print_file


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

            with captured_stdout() as stdout:
                # 実行
                print_file(fp.name, 2)

            # 検証
            expected = 'aaa\nbbb\n'
            actual = stdout.getvalue()
            self.assertEqual(expected, actual)
