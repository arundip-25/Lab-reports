def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def even_index_primes(lst):
    result = []
    for i in range(0, len(lst), 2):
        if is_prime(lst[i]):
            result.append(lst[i])
    return result

n = int(input("Enter number of elements: "))
numbers = []

for _ in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

output = even_index_primes(numbers)
print("Prime numbers at even indexes:", output)
