import pandas as pd
import random


def load_data():
    df = pd.read_excel("Lab Session Data (2).xlsx",
                       sheet_name="marketing_campaign")
    return df


def distance(a, b):

    total = 0

    for i in range(len(a)):
        total = total + (a[i] - b[i]) ** 2

    return total ** 0.5


def assign_clusters(data, centroids):

    clusters = []

    for row in data:

        min_dist = distance(row, centroids[0])
        cluster = 0

        for i in range(1, len(centroids)):

            d = distance(row, centroids[i])

            if d < min_dist:
                min_dist = d
                cluster = i

        clusters.append(cluster)

    return clusters


def new_centroids(data, clusters, k):

    centroids = []

    for i in range(k):

        group = []

        for j in range(len(data)):
            if clusters[j] == i:
                group.append(data[j])

        if len(group) == 0:
            centroids.append(random.choice(data))
        else:

            center = []

            for col in range(len(group[0])):

                total = 0

                for row in group:
                    total += row[col]

                center.append(total / len(group))

            centroids.append(center)

    return centroids


def kmeans(data, k, iterations):

    centroids = random.sample(data, k)

    for i in range(iterations):

        clusters = assign_clusters(data, centroids)

        centroids = new_centroids(data, clusters, k)

    return clusters, centroids


def main():

    df = load_data()

    data = df.select_dtypes(include=["number"])

    data = data.fillna(data.mean())

    data = data.values.tolist()

    k = 3

    clusters, centroids = kmeans(data, k, 10)

    print("Cluster of First 20 Records")

    for i in range(20):
        print("Record", i + 1, ":", clusters[i])

    print()

    print("Centroids")

    for i in range(len(centroids)):
        print("Cluster", i)
        print(centroids[i])


main()