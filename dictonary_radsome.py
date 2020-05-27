mn = input().split()

m = int(mn[0])

n = int(mn[1])

magazine = input().rstrip().split()

note = input().rstrip().split()

for x in note:
    if (x in magazine):
        print(x)
        magazine.remove(x)

    else:
        print("No")
        break
print("Yes")
