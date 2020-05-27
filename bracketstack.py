

def isBalanced(s):
    l = ["0"]
    x = 0
    for i in s:

        if(i == "}"):

            if("{" == l[-1]):

                del l[-1]

            else:
                return "NO"
        elif(i == ")"):

            if("(" == l[-1]):

                del l[-1]

            else:
                return "NO"
        elif(i == "]"):

            if("[" == l[-1]):

                del l[-1]

            else:
                return "NO"
        else:
            l.append(i)

    if(len(l) == 1):
        return "YES"
    return "NO"


t = int(input(""))
for _ in range(t):
    s = input("")
    print(isBalanced(s), end="")
