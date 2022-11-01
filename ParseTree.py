class ParseNode:
    def __init__(self, value=""):
        """Initializes a node with empty left and right pointers"""
        self.value = value
        self.leftNode = None
        self.rightNode = None
    
    def getValue(self):
        """Returns the value stored within a node"""
        return self.value

    def getLeft(self):
        """Returns the left node"""
        return self.leftNode

    def getRight(self):
        """Returns the right node"""
        return self.rightNode

    def setValue(self, value):
        """Sets the value stored within a node"""
        self.value = value

    def setLeft(self, other):
        """Sets the left node"""
        self.leftNode = other

    def setRight(self, other):
        """Sets the right node"""
        self.rightNode = other

class ParseTree:
    def __init__(self, expression=""):
        """Initializes an empty parse tree"""
        stack = []
        for i in expression:
            if i == "":
                continue
            elif i in ("+", "-", "*", "/"):
                temp = ParseNode(i)
                tempPopRight = stack.pop()
                tempPopLeft = stack.pop()
                temp.setRight(tempPopRight)
                temp.setLeft(tempPopLeft)
                stack.append(temp)
            else:
                temp = ParseNode(i)
                stack.append(temp)
        self.root = stack.pop()

    def preOrder(self):
        """return a string containing a prefix version of the expression. This must be a recursive method
        pre-order visits the node, then the left subtree, then the right subtree"""

    def inOrder(self):
        """ return a string containing an infix version of the expression, remember to add parentheses. This must be a recursive method.
        in-order visits the left subtree, then the node, then the right subtree
        """
    
    def postOrder(self):
        """return a string containing a postfix version of the expression. This must be a recursive method
        post-order visits the left subtree, then the right subtree, then the node"""

            
"""
Look at each character in the string in order 
• If a space 
o do nothing 
• If an operand 
o create a new node for the operand 
o push it on the stack 
• If an operator 
o create a new node for the operator 
o pop the top of the stack and attach it on the right of the new node 
o pop the top of the stack and attach it on the left of the new node 
o push new node and its subtree on the stack 
• If end of expression 
o pop the top of the stack and save the node as root of the tree 
"""            