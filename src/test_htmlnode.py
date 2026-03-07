import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def setUp(self):
        self.props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        self.node = HTMLNode("a", "test", None, self.props)
    
    def test_repr(self):
        self.assertEqual(str(self.node), f"HTMLNode(a, test, children: None, {self.props})")
    
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )
    
    def test_to_html(self):
        with self.assertRaises(NotImplementedError):
            self.node.to_html()

    def test_props_to_html(self):
        self.assertEqual(self.node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")


if __name__ == "__main__":
    unittest.main()
