from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a tag.")
        
        if not self.children:
            raise ValueError("All parent nodes must have children.")
        
        cldn_str = ""

        for child in self.children:
            cldn_str += child.to_html()
        
        return f"<{self.tag}>{cldn_str}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
