import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        self.assertTrue(HTMLNode("p", "Test", [], {}).props_to_html() == "")
        self.assertTrue(HTMLNode("p", "Test", [], {"a": "b", "c": "d"}).props_to_html() == "a=\"b\" c=\"d\"")
        self.assertTrue(HTMLNode("p", "Test", [], {"a": "b", "c": "d", "e": "f"}).props_to_html() == "a=\"b\" c=\"d\" e=\"f\"")
    
    def test_leaf_to_html(self):
        self.assertEqual(LeafNode("p", "Test").to_html(), "<p>Test</p>")
        self.assertEqual(LeafNode("a", "Link", {"href": "www.google.com"}).to_html(), "<a href=\"www.google.com\">Link</a>")
        self.assertEqual(LeafNode("h1", "Header", {"style": "dark", "font": "calibri"}).to_html(), "<h1 style=\"dark\" font=\"calibri\">Header</h1>")
        with self.assertRaises(ValueError):
            LeafNode("h1", None, {"style": "dark", "font": "calibri"}).to_html()
    
    def test_parent_to_html(self):
        parent1 = ParentNode("p", [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text")
        ])
        parent2 = ParentNode(None, ("b", "Bold text"))
        parent3 = ParentNode("p", None)
        self.assertEqual(parent1.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        with self.assertRaises(ValueError):
            parent2.to_html()
            parent3.to_html()
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )




if __name__ == "__main__":
    unittest.main()