def productPrimeFactors(n, product):

    for i in range(2, n+1):
        if (n % i == 0):
            isPrime = 1

            for j in range(2, int(i/2 + 1)):
                if (i % j == 0):
                    isPrime = 0
                    break

            # condition if \'i\' is Prime number
            # as well as factor of num
            if (isPrime):
                product += 1
    print(product)
    return product


# main()
n = 30
product = 0
print(productPrimeFactors(n, 0))
