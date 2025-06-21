import unittest
from blocks import (
    BlockType, 
    markdown_to_blocks, 
    block_to_block_type,
    markdown_to_html_node
)

class TestBlocks(unittest.TestCase):
    def test_md_to_blocks(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""
        self.assertEqual(markdown_to_blocks(markdown), [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
            "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        ])

    def test_block_to_block_type_paragraph(self):
        markdown = "This is a paragraph of text. It has some **bold** and _italic_ words inside of it."
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_block_to_block_type_header(self):
        markdown = "# This is a heading"
        self.assertEqual(block_to_block_type(markdown), BlockType.HEADING)
    
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        markdown = ">This is\n>a quote"
        self.assertEqual(block_to_block_type(markdown), BlockType.QUOTE)
    
    def test_block_block_type_unordered_list(self):
        markdown = "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        self.assertEqual(block_to_block_type(markdown), BlockType.ULIST)

    def test_block_block_type_ordered_list(self):
        markdown = "1. This is the first list item in a list block\n2. This is a list item\n3. This is another list item"
        self.assertEqual(block_to_block_type(markdown), BlockType.OLIST)


    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>")


    def test_special_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here
And an ![image](www.ea.com)

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here And an </p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>")
    
    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = "### This is a level 3 heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>This is a level 3 heading</h3></div>"
        )
    
    def test_heading2(self):
        md = "###### This is a level 6 heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>This is a level 6 heading</h6></div>"
        )

    def test_special_heading(self):
        md = "### This is a level 3 heading with an _italic_ text"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>This is a level 3 heading with an <i>italic</i> text</h3></div>"
        )
    
    def test_quote(self):
        md = """
> This is
> A quote
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is A quote</blockquote></div>"
        )

    def test_special_quote(self):
        md = """
> This is
> A **special** quote
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is A <b>special</b> quote</blockquote></div>"
        )
    
    def test_unordered_list(self):
        md = """
- This is
- Something
- For sure
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is</li><li>Something</li><li>For sure</li></ul></div>"
        )

    def test_special_unordered_list(self):
        md = """
- This is
- _Trouble_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is</li><li><i>Trouble</i></li></ul></div>"
        )
    
    def test_ordered_list(self):
        md = """
1. This is
2. Another thing
3. For sure
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is</li><li>Another thing</li><li>For sure</li></ol></div>"
        )
    
    def test_special_ordered_list(self):
        md = """
1. This is
2. Another thing with **bold**
3. For sure
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is</li><li>Another thing with <b>bold</b></li><li>For sure</li></ol></div>"
        )
    
