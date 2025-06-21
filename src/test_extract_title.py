import unittest

from extract_title import extract_title

class TestHTMLNode(unittest.TestCase):
    def test1(self):
        md = """
This text has
0 Headings
At all
"""
        with self.assertRaises(Exception):
            extract_title(md)

    def test2(self):
        md = """
This text has
# A Heading
"""
        self.assertEqual(extract_title(md), "A Heading")
    
    def test3(self):
        md = """
This text has
#An Improper Heading
"""
        with self.assertRaises(Exception):
            extract_title(md)