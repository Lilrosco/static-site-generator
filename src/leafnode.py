from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value.")

        if not self.tag:
            return self.value
        
        if self.tag == "a":
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()} />"

        return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
