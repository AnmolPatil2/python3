def combination(iterable, r):

    pool = tuple(iterable)
    n = len(pool)

    if r > n:
        return
    indices = range(r)
    print(indices[0])

    yield tuple(pool[i] for i in indices)

    while True:
        for i in reversed(range(r)):
            print(indices[i])
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


print("s")
for x in combination("abc", 2):
    print(x)
