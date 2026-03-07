import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def setUp(self):
        self.props = {
            "href": "https://www.google.com",
        }
        self.node = LeafNode("p", "Hello, world!")
    
    def test_leaf_to_html_p(self):
        self.assertEqual(self.node.to_html(), "<p>Hello, world!</p>")
    
    def test_repr(self):
        self.node.props = self.props
        self.assertEqual(str(self.node), f"LeafNode(p, Hello, world!, {self.props})")
    
    def test_to_html(self):
        self.node.value = None
        with self.assertRaises(ValueError):
            self.node.to_html()

        self.node.value = ""
        with self.assertRaises(ValueError):
            self.node.to_html()

    def test_props_to_html_a(self):
        self.node.tag = "a"
        self.node.value = "Click me!"
        self.node.props = self.props
        self.assertEqual(self.node.to_html(), '<a href="https://www.google.com">Click me!</a>')


if __name__ == "__main__":
    unittest.main()
