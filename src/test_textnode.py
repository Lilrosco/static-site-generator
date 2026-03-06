import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(str(node), "TextNode(This is some anchor text, link, https://www.boot.dev)")
    
    def test_url_is_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)

    def test_url_is_not_none(self):
        url = "https://www.boot.dev"
        node = TextNode("This is some anchor text", TextType.LINK, url)
        self.assertIsNotNone(node.url)
        self.assertEqual(node.url, url)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

        node3 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node3)



if __name__ == "__main__":
    unittest.main()
