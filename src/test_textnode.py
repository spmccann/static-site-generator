import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_eq_none(self):
        node = TextNode("words here", "italic", None)
        node2 = TextNode("words here", "italic", None)
        self.assertEqual(node, node2)
    
    def test_eq_false(self):
        node = TextNode("words", "bold")
        node2 = TextNode("other words", "bold")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
