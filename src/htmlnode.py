class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        to_string = ""
        if self.props != None:
            for key, value in self.props.items():
                to_string += f" {key}='{value}'" 
        return to_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes require a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        left = f"<{self.tag}{self.props_to_html()}>"
        right = f"</{self.tag}>"
        html_string = "" 
        if self.tag == None:
            raise ValueError("No tag provided")
        if self.children == None:
            raise ValueError("No children")
        for child in self.children:
            html_string += child.to_html() 
        return left + html_string + right 
                
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"


