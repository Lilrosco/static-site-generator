import unittest

from main import extract_title

class TestMain(unittest.TestCase):
    def test_extract_title(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        header = extract_title(md)
        self.assertEqual(header, "this is an h1")
    
    def test_extract_title_no_headers(self):
        md = """
this is an h1

this is paragraph text

this is an h2
"""

        with self.assertRaises(ValueError) as ve:
            extract_title(md)
            self.assertEqual(str(ve), "Header 1 is not found in markdown")
    
    def test_extract_title_no_h1_header(self):
        md = """
## this is an h1

this is paragraph text
"""

        with self.assertRaises(ValueError) as ve:
            extract_title(md)
            self.assertEqual(str(ve), "Header 1 is not found in markdown")
