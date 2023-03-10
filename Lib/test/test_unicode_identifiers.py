import unittest

class PEP3131Test(unittest.TestCase):

    # TODO: RUSTPYTHON
    @unittest.expectedFailure
    def test_valid(self):
        class T:
            รค = 1
            ยต = 2 # this is a compatibility character
            ่ = 3
            x๓  = 4
        self.assertEqual(getattr(T, "\xe4"), 1)
        self.assertEqual(getattr(T, "\u03bc"), 2)
        self.assertEqual(getattr(T, '\u87d2'), 3)
        self.assertEqual(getattr(T, 'x\U000E0100'), 4)

    # TODO: RUSTPYTHON
    @unittest.expectedFailure
    def test_non_bmp_normalized(self):
        ๐๐ซ๐ฆ๐ ๐ฌ๐ก๐ข = 1
        self.assertIn("Unicode", dir())

    # TODO: RUSTPYTHON
    @unittest.expectedFailure
    def test_invalid(self):
        try:
            from test import badsyntax_3131
        except SyntaxError as err:
            self.assertEqual(str(err),
              "invalid character 'โฌ' (U+20AC) (badsyntax_3131.py, line 2)")
            self.assertEqual(err.lineno, 2)
            self.assertEqual(err.offset, 1)
        else:
            self.fail("expected exception didn't occur")

if __name__ == "__main__":
    unittest.main()
