import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    # SECTION HTML

    def test_values(self):
        node = HTMLNode(
            "p",
            "test val"
        )
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "test val")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_props_to_html(self):
        node = HTMLNode(
            "div",
            "test",
            "None",
            {"class": "test"}
        )
        self.assertEqual(
            node.props_to_html(),
            " class='test'" 
        )

    def test_repr(self):
        node = HTMLNode(
            "h1",
            "value",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(h1, value, children: None, {'class': 'primary'})",
        )

    # SECTION Leaf

    def test_eq(self):
        node = LeafNode(
            "p",
            "paragraph"
        )
        self.assertEqual(
            node.to_html(),
            "<p>paragraph</p>"
        )

    def test_eq_props(self):
        node = LeafNode(
            "a",
            "google",
            {"href": "https://www.google.com"}
        )
        self.assertEqual(
            node.to_html(),
            "<a href='https://www.google.com'>google</a>"
        )

    # SECTION PARENT

    def test_to_html_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

if __name__ == "__main__":
    unittest.main()