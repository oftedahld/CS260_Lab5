from ParseTree import ParseTree


display = True

def main():
    # uncomment tests to run

    testBase()
    testAdv()
    testThink()

def testBase():
    print("Testing Base Parse Tree\n")
    
    expression1 = "AB+CD-*"
    expression2 = "AB-C+DE/*"
    
    ptree1 = ParseTree(expression1)
    print("\nInput is AB+CD-* ")
    print("In Order should be (A+B)*(C-D) or (A+B)*(C-D) or (((A)+(B))*((C)-(D))) \n   and is ", ptree1.inOrder())
    print("Post Order should be AB+CD-* and is ", ptree1.postOrder())
    print("Pre Order should be *+AB-CD and is ", ptree1.preOrder())
    
    if display:
        print(ptree1.display())
    
    ptree2 = ParseTree(expression2)
    print("\nInput is AB-C+DE/* ")
    print("In Order output should be (A-B+C)*D/E or ((A-B)+C)*(D/E) or ((((A)-(B))+(C))*((D)/(E))) \n   and is ",ptree2.inOrder())
    print("Post Order should be AB-C+DE/* and is ", ptree2.postOrder())
    print("Pre Order should be *+-ABC/DE and is ", ptree2.preOrder())
    
    if display:
        print(ptree2.display())
    
    print("\nDone with Parse Tree test\n")


def testAdv():
    print("Testing Advanced Parse Tree")
    
    expression3 = "(A+B)*C+D"
    expression4 = "A/(B+C)*(D+E)"
    expression5 = "A/((B+C)*(D+E))"
    ptree3 = ParseTree("")
    
    ptree3.parseInOrder(expression3)
    print("Input is (A+B)*C+D")
    print("In Order should be (A+B)*C+D or (((A+B)*C)+D) or ((((A)+(B))*(C))+(D)) \n   and is " + ptree3.inOrder())
    print("Post Order should be AB+C*D+ and is " + ptree3.postOrder())
    print("Pre Order should be +*+ABCD and is " + ptree3.preOrder(), end="\n\n")
    
    if display:
        print(ptree3.display())

    ptree3.parseInOrder(expression4)
    print("Input is A/(B+C)*(D+E)" )
    print("IIn Order should be A/(B+C)*(D+E) or ((A/(B+C))*(D+E)) or (((A)/((B)+(C)))*((D)+(E))) \n   and is " + ptree3.inOrder())
    print("Post Order should be ABC+/DE+* and is " + ptree3.postOrder())
    print("Pre Order should be */A+BC+DE and is " + ptree3.preOrder(), end="\n\n")
    
    if display:
        print(ptree3.display())
    
    ptree3.parseInOrder(expression5)
    print("Input is A/((B+C)*(D+E))" )
    print("In Order should be A/((B+C)*(D+E)) or (A/((B+C)*(D+E))) or ((A)/(((B)+(C))*((D)+(E)))) \n   and is " + ptree3.inOrder())
    print("Post Order should be ABC+DE+*/ and is " + ptree3.postOrder())
    print("Pre Order should be /A*+BC+DE and is " + ptree3.preOrder(), end="\n\n")
    
    if display:
        print(ptree3.display())

    print("Done with Advanced Parse Tree test", end="\n\n")
    

def testThink():
    print("Testing Thinking Problem", end="\n\n")

    expression6 = "(((A+B)*C)+(D*(F/G)))"
    expression7 = "((A*B)+(C-D))"
    expression8 = "(A-(B-C))"
    ptree4 = ParseTree("")

    ptree4.parseInOrder(expression6)
    print("Input is (((A+B)*C)+(D*(F/G)))")
    print("In Order should be (A+B)*C+D*F/G and is " + ptree4.inOrder(), end="\n\n")
    print("Post Order should be AB+C*DFG/*+ and is " + ptree4.postOrder())
    print("Pre Order should be +*+ABC*D/FG and is " + ptree4.preOrder(), end="\n\n")
    
    if display:
        print(ptree4.display())

    ptree4.parseInOrder(expression7)
    print("Input is ((A*B)+(C-D))")
    print("In Order should be A*B+C-D and is " + ptree4.inOrder(), end="\n\n")
    print("Post Order should be AB*CD-+ and is " + ptree4.postOrder())
    print("Pre Order should be +*AB-CD and is " + ptree4.preOrder(), end="\n\n")
    
    if display:
        print(ptree4.display())
    
    ptree4.parseInOrder(expression8)
    print("Input is (A-(B-C))")
    print("In Order should be A-(B-C) and is " + ptree4.inOrder(), end="\n\n")
    print("Post Order should be ABC-- and is " + ptree4.postOrder())
    print("Pre Order should be -A-BC and is " + ptree4.preOrder(), end="\n\n")
    
    if display:
        print(ptree4.display())

    print("Done with Testing Thinking Problem", end="\n\n")


if __name__ == '__main__':
    main()