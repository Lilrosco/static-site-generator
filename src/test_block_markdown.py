import unittest

from block_markdown import *

class MarkdownToBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class BlockToBlockType(unittest.TestCase):
    def test_block_to_block_types(self):
            block = "# heading"
            self.assertEqual(block_to_block_type(block), BlockType.HEADING)
            block = "```\ncode\n```"
            self.assertEqual(block_to_block_type(block), BlockType.CODE)
            block = "> quote\n> more quote"
            self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
            block = "- list\n- items"
            self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
            block = "1. list\n2. items"
            self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
            block = "paragraph"
            self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

#     def test_headings(self):
#         md = """
# ##### Heading 5
# #### Heading 4
# ### Heading 3
# ## Heading 2
# # Heading
# """
#         blocks = markdown_to_blocks(md)

#         for block in blocks:
#             self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
#     def test_invalid_heading(self):
#         block = "###Bad Heading"

#         self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
#     def test_code(self):
#         block = """
# ```
# print("Hello, world!")
# ```
# """

#         self.assertEqual(block_to_block_type(block), BlockType.CODE)

#     def test_quote(self):
#         block = """
# > This is a block quote.
# """

#         self.assertEqual(block_to_block_type(block), BlockType.QUOTE)


if __name__ == "__main__":
    unittest.main()
