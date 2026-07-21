import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time


def load_data(filename, sheet_name="IRCTC Stock Price"):
    df = pd.read_excel(filename, sheet_name=sheet_name)
    return df.dropna(subset=["Price"])


def custom_mean(data):
    total = 0
    count = 0
    for value in data:
        total += value
        count += 1
    return total / count


def custom_variance(data):
    mean = custom_mean(data)
    total = 0
    count = 0
    for value in data:
        total += (value - mean) ** 2
        count += 1
    return total / count


def numpy_mean(data):
    return np.mean(data)


def numpy_variance(data):
    return np.var(data)


def average_execution_time(function, data, runs=10):
    total_time = 0
    for _ in range(runs):
        start = time.perf_counter()
        function(data)
        end = time.perf_counter()
        total_time += (end - start)
    return total_time / runs


def get_wednesday_mean(df):
    wednesday_data = df[df["Day"] == "Wed"]
    return custom_mean(wednesday_data["Price"])


def get_april_mean(df):
    april_data = df[df["Month"] == "Apr"]
    return custom_mean(april_data["Price"])


def compare_means(sample_mean, population_mean, label):
    if sample_mean > population_mean:
        print(f"Observation: {label} mean is greater than population mean.")
    elif sample_mean < population_mean:
        print(f"Observation: {label} mean is smaller than population mean.")
    else:
        print(f"Observation: {label} mean is equal to population mean.")


def get_probability_of_loss(df):
    loss_days = list(filter(lambda x: x < 0, df["Chg%"]))
    return len(loss_days) / len(df)


def get_probability_profit_wednesday(df):
    wednesday = df[df["Day"] == "Wed"]
    profit_wednesday = wednesday[wednesday["Chg%"] > 0]
    return len(profit_wednesday) / len(df), wednesday, profit_wednesday


def get_conditional_probability(profit_wednesday, wednesday):
    return len(profit_wednesday) / len(wednesday)


def plot_chg_vs_day(df):
    plt.figure(figsize=(10, 5))
    plt.scatter(df["Day"], df["Chg%"])
    plt.xlabel("Day of Week")
    plt.ylabel("Chg %")
    plt.title("Chg% vs Day of Week")
    plt.grid(True)
    plt.show()


def print_mean_variance_results(np_mean, my_mean, np_variance, my_variance):
    print("\nPopulation Mean (NumPy):", np_mean)
    print("Population Mean (Custom):", my_mean)
    print("\nPopulation Variance (NumPy):", np_variance)
    print("Population Variance (Custom):", my_variance)


def print_execution_times(numpy_mean_time, custom_mean_time,
                           numpy_variance_time, custom_variance_time):
    print("\nAverage Execution Time (10 Runs)")
    print("\nMean")
    print("NumPy Mean :", numpy_mean_time)
    print("Custom Mean:", custom_mean_time)
    print("\nVariance")
    print("NumPy Variance :", numpy_variance_time)
    print("Custom Variance:", custom_variance_time)


def main():
    filename = "Lab Session Data .xlsx"

    df = load_data(filename)
    price = df["Price"]

    np_mean = numpy_mean(price)
    np_variance = numpy_variance(price)

    my_mean = custom_mean(price)
    my_variance = custom_variance(price)

    print_mean_variance_results(np_mean, my_mean, np_variance, my_variance)

    numpy_mean_time = average_execution_time(numpy_mean, price)
    custom_mean_time = average_execution_time(custom_mean, price)

    numpy_variance_time = average_execution_time(numpy_variance, price)
    custom_variance_time = average_execution_time(custom_variance, price)

    print_execution_times(numpy_mean_time, custom_mean_time,
                           numpy_variance_time, custom_variance_time)

    wednesday_mean = get_wednesday_mean(df)
    print("\nWednesday Sample Mean:", wednesday_mean)
    compare_means(wednesday_mean, my_mean, "Wednesday")

    april_mean = get_april_mean(df)
    print("\nApril Sample Mean:", april_mean)
    compare_means(april_mean, my_mean, "April")

    probability_loss = get_probability_of_loss(df)
    print("\nProbability of Loss:", probability_loss)

    probability_profit_wednesday, wednesday, profit_wednesday = get_probability_profit_wednesday(df)
    print("\nProbability of Profit on Wednesday:", probability_profit_wednesday)

    conditional_probability = get_conditional_probability(profit_wednesday, wednesday)
    print("\nConditional Probability (Profit | Wednesday):", conditional_probability)

    plot_chg_vs_day(df)


main()