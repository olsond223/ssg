import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(TextNode("This is a text node", TextType.BOLD), 
                         TextNode("This is a text node", TextType.BOLD))
        self.assertNotEqual(TextNode("This is not a text node", TextType.BOLD), 
                         TextNode("This is a text node", TextType.BOLD))
        self.assertNotEqual(TextNode("This is a text node", TextType.BOLD), 
                         TextNode("This is a text node", TextType.ITALIC))
        self.assertNotEqual(TextNode("This is a text node", TextType.BOLD, "html.com"), 
                         TextNode("This is a text node", TextType.ITALIC))
        self.assertNotEqual(TextNode("This is a text node", TextType.BOLD, "html.com"), 
                         TextNode("This is a text node", TextType.BOLD, "tml.com"))
    
    def test_text(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        node = TextNode("This is code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        node = TextNode("This is link text", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.props, {"href": "www.google.com"})
        node = TextNode("This is image text", TextType.IMAGE, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.props, {"src": "www.google.com", "alt": "This is image text"})

if __name__ == "__main__":
    unittest.main()