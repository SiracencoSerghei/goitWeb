import concurrent.futures
import math

PRIMES = [
    13,
    11,
    15,
    17,
    19,
    10]


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    executor = concurrent.futures.ProcessPoolExecutor(4)
    # zip_dict = zip(PRIMES, executor.map(is_prime, PRIMES))
    # for key, values in zip_dict:
    #     print(f"{key}: {values}")

    zip_dict = zip(PRIMES, executor.map(is_prime, PRIMES))

    with executor:
        for number, prime in zip_dict:
            print('%d is prime: %s' % (number, prime))
