import math
start = 11
end = int(math.sqrt(25))+1
l = []
for val in range(2, end + 1):
    if val > 1:
        for n in range(2, val//2 + 2):
            if (val % n) == 0:
                break
            else:
                if n == val//2 + 1:
                    l.append(val)
print(min(l))
