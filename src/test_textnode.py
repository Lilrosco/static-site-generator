import unittest

from textnode import TextNode, TextType, text_node_to_html_node

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

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.to_html(), "<b>This is a text node</b>")
    
    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.to_html(), "<i>This is a text node</i>")
    
    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.to_html(), "<code>This is a text node</code>")
    
    def test_link(self):
        node = TextNode("This is a text node with a link", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node with a link")
        self.assertEqual(html_node.to_html(), '<a href="https://www.google.com">This is a text node with a link</a>')
    
    def test_image(self):
        node = TextNode("This is a text node of an image", TextType.IMAGE, "some/image/location/img.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.to_html(), '<img src="some/image/location/img.jpg" alt="This is a text node of an image" />')
    
    def test_invalid_text_type(self):
        node = TextNode("This is a text node of an image", "FAKE")

        with self.assertRaises(Exception) as e:
            text_node_to_html_node(node)

            self.assertEqual(str(e), "Invalid Text Type")


if __name__ == "__main__":
    unittest.main()
