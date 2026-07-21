import random
import statistics


def generate_numbers():
    return [random.randint(1, 10) for _ in range(25)]


def calculate_statistics(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    mode = statistics.mode(numbers)

    return mean, median, mode


def main():
    numbers = generate_numbers()

    print("Random Numbers:")
    print(numbers)

    mean, median, mode = calculate_statistics(numbers)

    print("Mean =", mean)
    print("Median =", median)
    print("Mode =", mode)


main()