from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a tag.")
        
        if not self.children:
            raise ValueError("All parent nodes must have children.")
        
        child_html = ""

        for child in self.children:
            child_html += child.to_html()
        
        return f"<{self.tag}>{child_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
