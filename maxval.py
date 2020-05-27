def findn(k):
    kl = [1, 1]
    i = 1
    while kl[i]+kl[i-1] <= k:
        kl.append(kl[i]+kl[i-1])
        i += 1
        print(kl)
    jk = [1, 2]
    j = 1
    while j < i:
        jk.append(jk[j]+jk[j-1])
        j += 1
        print(jk)

    return jk[-1]


k = int(input())
print(findn(k))
