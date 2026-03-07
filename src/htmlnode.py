class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        rtn_str = ""

        if not self.props:
            return rtn_str
        
        for key, value in self.props.items():
            rtn_str += f" {key.strip("\"")}=\"{value}\""
        
        return rtn_str
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
