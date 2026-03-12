import unittest

from gencontents import extract_title

class TestGenerateContent(unittest.TestCase):
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


    def test_eq(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    def test_eq_double(self):
        actual = extract_title(
            """
# This is a title

# This is a second title that should be ignored
"""
        )
        self.assertEqual(actual, "This is a title")

    def test_eq_long(self):
        actual = extract_title(
            """
# title

this is a bunch

of text

- and
- a
- list
"""
        )
        self.assertEqual(actual, "title")

    def test_none(self):
        try:
            extract_title(
                """
no title
"""
            )
            self.fail("Should have raised an exception")
        except Exception as e:
            pass
