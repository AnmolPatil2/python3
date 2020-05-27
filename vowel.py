t = int(input(""))
vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
for _ in range(t):
    l = list(input(""))
    l.sort()
    x = 0
    while(x < (len(l))):
        d = 5
        if(l[x] in vowels):
            l[x] = chr(ord(l[x])+x)

            if(l[x] in vowels):
                if(d == 0):
                    print("NO")
                d -= 1
            else:
                x += 1
        else:
            x += 1
    listToStr = ''.join(map(str, l))
    print(listToStr)
