
def abbreviation(a, b):
    l = []
    l1 = []
    for i in range(len(a)):
        if(a[i].isupper()):
            if(a[i] not in b):
                return "NO"
            else:
                l.append(b.index(a[i]))

        else:

            l1.append(a[i])

    for i in range(len(b)):
        if(i in l):
            continue
        x = b[i].lower()
        print(x)

        if(x not in l1):
            return "NO"
    return "YES"


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        a = list(input())

        b = list(input())

        result = abbreviation(a, b)
        print(result)
