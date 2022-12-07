def sum_of_odd_factors(num):
    odd_factors = []
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 != 0:
            odd_factors.append(i)
    return sum(odd_factors)


if __name__ == "__main__":
    print(sum_of_odd_factors(18))
