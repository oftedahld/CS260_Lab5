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
        root = ParseNode()
        for i in range(0, len(expression)):
            value = expression[i]
            if value == " ":
                continue #skip if space
            if value.isAlpha() == True:
                """If alpha character"""
                value = value.upper() #Convert to upper case for consistency
                operandNode = ParseNode(i)
            if value == "+" or value == "-" or value == "*" or value == "/":
                operatorNode = ParseNode(i)



        