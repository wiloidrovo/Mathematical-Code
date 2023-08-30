def validate_expr(S):
    stack = []
    good = True
    i = 0
    while good and len(S) > i:
        if (S[i]== "("):
            stack.append("(")
        elif (S[i]==")"):
            if (len(stack) == 0):
                good = False
            else:
                stack.pop()
        i += 1
    if (not(len(stack)==0)):
        good = False
    return good
S = str(input("Ingrese la expresion: "))
Validate = validate_expr(S)
print(Validate)