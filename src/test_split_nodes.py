import unittest
from textnode import *
from split_nodes import *

class TestSplitNodes(unittest.TestCase):
    def test_delimiter(self):
        node1 = TextNode("What is the point _of_ all of this?", TextType.TEXT)
        node2 = TextNode("This is **a** test", TextType.TEXT)
        node3 = TextNode("We don't `do anything` else these days", TextType.TEXT)

        node_list = [node1, node2, node3]
        self.assertEqual(split_nodes_delimiter(node_list, "**", TextType.BOLD), [
        TextNode("What is the point _of_ all of this?", TextType.TEXT, None), 
        TextNode("This is ", TextType.TEXT, None), 
        TextNode("a", TextType.BOLD, None), 
        TextNode(" test", TextType.TEXT, None), 
        TextNode("We don't `do anything` else these days", TextType.TEXT, None)
        ])

    def test_image(self):
        node1 = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT) 
        node2 = TextNode("and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
        node_list = [node1, node2]
        self.assertEqual(split_nodes_image(node_list), [
            TextNode("This is text with an ", TextType.TEXT, None),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode("and another ", TextType.TEXT, None),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
        ])

    def test_image2(self):
        node1 = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
        node_list = [node1]
        self.assertEqual(split_nodes_image(node_list), [
            TextNode("This is text with an ", TextType.TEXT, None),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT, None),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
        ])
    
    def test_mixed_image(self):
        node1 = TextNode("This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and an image ![image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
        node_list = [node1]
        self.assertEqual(split_nodes_image(node_list), [
            TextNode("This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and an image ", TextType.TEXT, None),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
        ])

    def test_link(self):
        node1 = TextNode("This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
        node_list = [node1]
        self.assertEqual(split_nodes_link(node_list), [
            TextNode("This is text with a ", TextType.TEXT, None),
            TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT, None),
            TextNode("second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png")
        ])
    
    def test_mixed_link(self):
        node1 = TextNode("This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and an image ![image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
        node_list = [node1]
        self.assertEqual(split_nodes_link(node_list), [
            TextNode("This is text with a ", TextType.TEXT, None),
            TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and an image ![image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT, None)
        ])
    
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertEqual(text_to_textnodes(text), [
            TextNode("This is ", TextType.TEXT, None),
            TextNode("text", TextType.BOLD, None),
            TextNode(" with an ", TextType.TEXT, None),
            TextNode("italic", TextType.ITALIC, None),
            TextNode(" word and a ", TextType.TEXT, None),
            TextNode("code block", TextType.CODE, None),
            TextNode(" and an ", TextType.TEXT, None),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT, None),
            TextNode("link", TextType.LINK, "https://boot.dev")
        ])

