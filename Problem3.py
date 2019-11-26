def sum_of_squares(n):
    return sum(list(map(lambda x: x*x, list(range(1, n+1)))))


def square_of_the_sum(n):
    return sum(list(range(1, n+1)))**2


if __name__ == '__main__':
    n = int(input())
    print(square_of_the_sum(n) - sum_of_squares(n))