import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_HTML(self):
        node = HTMLNode("p", "text here", None, {'href': 'https//boot.dev', 'target': '_blank'})
        self.assertEqual(node.props_to_html(), " href='https//boot.dev' target='_blank'")
    
class TestLeafNode(unittest.TestCase):
    def test_to_HTML(self):
        node = LeafNode("a", "this is the message", {'href': 'https//boot.dev'})
        self.assertEqual(node.to_html(), "<a href='https//boot.dev'>this is the message</a>")
    
    def test_to_HTML_propless(self):
        node = LeafNode("p", "another message")
        self.assertEqual(node.to_html(), "<p>another message</p>")

    def text_to_HTML_valueless(self):
        node = LeafNode("p", None, None)
        self.assertEqual(node.to_html(), ValueError)

class TestParentNode(unittest.TestCase):
    def test_to_html_parent(self):
        node = ParentNode("p",[LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text"),],)
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")


if __name__ == "__main__":
    unittest.main()


