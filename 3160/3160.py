"prime number"
S,E = map(int, input().split())
prime = []
for i in range(S, E + 1):
    if i > 1:
        for j in range(2, int(i/2) + 1):
            if not i % j:
                break
        else:
            prime.append(i)
if prime:
    print(" ".join(map(str, prime)))
print("Total primes:", len(prime))
