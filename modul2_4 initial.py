numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    is_prime = True
    if i == 1:
        continue

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime == True:
        primes.append(i)
    else:
        not_primes.append(i)

primes.insert(0, 1)

print("Primes: ", primes)
print("Not primes: ", not_primes)