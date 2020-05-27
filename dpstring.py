
def abbreviation(a, b):
    l = []
    l1 = {}
    l2 = []
    for i in range(len(a)):
        if(a[i].isupper()):
            if(a[i] not in b):
                return "NO"
            else:
                y = b.index(a[i])
                b[y] = 0

        else:

            if(a[i] in l1):
                l1[a[i]] += 1
            else:
                l1[a[i]] = 1

    for i in range(len(b)):
        if(b[i] == 0):
            continue
        x = b[i].lower()

        if(x not in l1):
            return "NO"
        else:
            l1[x] -= 1
            if(l1[x] == -1):
                return "NO"

    return "YES"


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        a = list(input())

        b = list(input())

        result = abbreviation(a, b)
        print(result)
