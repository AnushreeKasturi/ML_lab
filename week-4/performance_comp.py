# Generated with assistance from ChatGPT (OpenAI)

import numpy as np
import pandas as pd
import time


# ---------------------------------------------------------
# Load the marketing_campaign dataset
# ---------------------------------------------------------

file_path = r"C:\Users\anush\Downloads\sem5\ML_lab\week-2\Lab Session Data .xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="marketing_campaign"
)

print("Dataset shape:")
print(df.shape)


# ---------------------------------------------------------
# Select numerical features
# ---------------------------------------------------------

numeric_columns = df.select_dtypes(
    include=[np.number]
).columns.tolist()

# ID is only an identifier
if "ID" in numeric_columns:
    numeric_columns.remove("ID")

numeric_data = df[numeric_columns].copy()

# Handle missing values
numeric_data = numeric_data.fillna(
    numeric_data.median()
)

X = numeric_data.to_numpy(
    dtype=float
)


# ---------------------------------------------------------
# Standardize the data
# ---------------------------------------------------------

mean = np.mean(
    X,
    axis=0
)

std = np.std(
    X,
    axis=0
)

std[std == 0] = 1

X_kmeans = (
    X - mean
) / std


# =========================================================
# STUDENT K-MEANS IMPLEMENTATION
# =========================================================

def kmeans_student(
    X,
    k=3,
    max_iterations=100
):

    # Initialize centroids
    centroids = X[
        :k
    ].copy()

    for iteration in range(
        max_iterations
    ):

        # Assignment step
        labels = []

        for point in X:

            distances = []

            for centroid in centroids:

                distance = np.sqrt(
                    np.sum(
                        (point - centroid) ** 2
                    )
                )

                distances.append(
                    distance
                )

            labels.append(
                np.argmin(distances)
            )

        labels = np.array(labels)


        # Update step
        new_centroids = []

        for cluster in range(k):

            cluster_points = X[
                labels == cluster
            ]

            if len(cluster_points) > 0:

                new_centroid = np.mean(
                    cluster_points,
                    axis=0
                )

            else:

                new_centroid = centroids[
                    cluster
                ]

            new_centroids.append(
                new_centroid
            )

        new_centroids = np.array(
            new_centroids
        )


        # Check convergence
        if np.allclose(
            centroids,
            new_centroids
        ):

            return (
                labels,
                new_centroids,
                iteration + 1
            )

        centroids = new_centroids

    return (
        labels,
        centroids,
        max_iterations
    )


# =========================================================
# AI K-MEANS IMPLEMENTATION
# =========================================================

def kmeans_ai(
    X,
    k=3,
    max_iterations=100
):

    # Initialize centroids
    centroids = X[
        :k
    ].copy()

    for iteration in range(
        max_iterations
    ):

        # Vectorized distance calculation
        distances = np.linalg.norm(
            X[:, np.newaxis, :] -
            centroids[np.newaxis, :, :],
            axis=2
        )

        # Assign points to nearest centroid
        labels = np.argmin(
            distances,
            axis=1
        )


        # Recalculate centroids
        new_centroids = np.array([
            X[labels == cluster].mean(
                axis=0
            )
            if np.any(
                labels == cluster
            )
            else centroids[cluster]

            for cluster in range(k)
        ])


        # Check convergence
        if np.allclose(
            centroids,
            new_centroids
        ):

            return (
                labels,
                new_centroids,
                iteration + 1
            )

        centroids = new_centroids

    return (
        labels,
        centroids,
        max_iterations
    )


# =========================================================
# PERFORMANCE COMPARISON
# =========================================================

print(
    "\n========== PERFORMANCE COMPARISON =========="
)


# ---------------------------------------------------------
# Student K-Means
# ---------------------------------------------------------

start_student = time.perf_counter()

labels_student, centroids_student, iterations_student = (
    kmeans_student(
        X_kmeans,
        k=3
    )
)

end_student = time.perf_counter()

student_time = (
    end_student -
    start_student
)


# ---------------------------------------------------------
# AI K-Means
# ---------------------------------------------------------

start_ai = time.perf_counter()

labels_ai, centroids_ai, iterations_ai = (
    kmeans_ai(
        X_kmeans,
        k=3
    )
)

end_ai = time.perf_counter()

ai_time = (
    end_ai -
    start_ai
)


# ---------------------------------------------------------
# Display Results
# ---------------------------------------------------------

print(
    f"Student K-Means Time: "
    f"{student_time:.6f} seconds"
)

print(
    f"AI K-Means Time: "
    f"{ai_time:.6f} seconds"
)

print(
    f"Student Iterations: "
    f"{iterations_student}"
)

print(
    f"AI Iterations: "
    f"{iterations_ai}"
)


# ---------------------------------------------------------
# Compare Performance
# ---------------------------------------------------------

print("\n========== ANALYSIS ==========")

if student_time < ai_time:

    print(
        "Student K-Means was faster."
    )

elif ai_time < student_time:

    print(
        "AI K-Means was faster."
    )

else:

    print(
        "Both implementations had approximately "
        "the same execution time."
    )


# ---------------------------------------------------------
# Compare Cluster Sizes
# ---------------------------------------------------------

print("\nStudent Cluster Sizes:")

for cluster in range(3):

    count = np.sum(
        labels_student == cluster
    )

    print(
        f"Cluster {cluster + 1}: "
        f"{count} customers"
    )


print("\nAI Cluster Sizes:")

for cluster in range(3):

    count = np.sum(
        labels_ai == cluster
    )

    print(
        f"Cluster {cluster + 1}: "
        f"{count} customers"
    )