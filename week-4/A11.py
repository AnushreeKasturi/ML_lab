# Generated with assistance from ChatGPT (OpenAI)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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

print("\nNumerical features used:")
print(numeric_columns)


# ---------------------------------------------------------
# Handle missing values
# ---------------------------------------------------------

numeric_data = df[numeric_columns].copy()

numeric_data = numeric_data.fillna(
    numeric_data.median()
)


# ---------------------------------------------------------
# Convert to NumPy array
# ---------------------------------------------------------

X = numeric_data.to_numpy(
    dtype=float
)


# ---------------------------------------------------------
# Normalize features
# ---------------------------------------------------------
# Normalization prevents large-scale features such as
# Income or expenditure from dominating the distance.

mean = np.mean(
    X,
    axis=0
)

std = np.std(
    X,
    axis=0
)

# Prevent division by zero
std[std == 0] = 1

X_scaled = (
    X - mean
) / std


# ---------------------------------------------------------
# K-Means Function
# ---------------------------------------------------------

def kmeans(X, k, max_iterations=100):

    # Initialize centroids using the first k observations
    centroids = X[
        :k
    ].copy()

    for iteration in range(
        max_iterations
    ):

        # -------------------------------------------------
        # Assignment step
        # -------------------------------------------------

        distances = np.zeros(
            (X.shape[0], k)
        )

        for i in range(
            X.shape[0]
        ):

            for j in range(k):

                distances[i, j] = np.linalg.norm(
                    X[i] - centroids[j]
                )

        labels = np.argmin(
            distances,
            axis=1
        )


        # -------------------------------------------------
        # Update step
        # -------------------------------------------------

        new_centroids = np.zeros_like(
            centroids
        )

        for j in range(k):

            cluster_points = X[
                labels == j
            ]

            if len(cluster_points) > 0:

                new_centroids[j] = np.mean(
                    cluster_points,
                    axis=0
                )

            else:

                new_centroids[j] = centroids[j]


        # -------------------------------------------------
        # Check convergence
        # -------------------------------------------------

        if np.allclose(
            centroids,
            new_centroids
        ):

            print(
                f"\nK-Means converged after "
                f"{iteration + 1} iterations."
            )

            break

        centroids = new_centroids

    return labels, centroids


# ---------------------------------------------------------
# Apply K-Means
# ---------------------------------------------------------

k = 3

labels, centroids = kmeans(
    X_scaled,
    k
)


# ---------------------------------------------------------
# Display Cluster Information
# ---------------------------------------------------------

print("\n========== K-MEANS CLUSTERING ==========")

print(
    f"Number of clusters: {k}"
)

print(
    "\nCluster sizes:"
)

for cluster in range(k):

    count = np.sum(
        labels == cluster
    )

    print(
        f"Cluster {cluster + 1}: "
        f"{count} customers"
    )


# ---------------------------------------------------------
# Add cluster labels to dataset
# ---------------------------------------------------------

df["Cluster"] = labels


print("\nFirst 10 customers with cluster labels:")

print(
    df[
        ["ID", "Cluster"]
    ].head(10)
)


# ---------------------------------------------------------
# Display Cluster Centers
# ---------------------------------------------------------

print("\nCluster Centroids:")

print(
    centroids
)


# ---------------------------------------------------------
# Visualization
# ---------------------------------------------------------
# Use two important spending features for visualization.

if (
    "MntWines" in df.columns
    and "MntMeatProducts" in df.columns
):

    plt.figure(
        figsize=(8, 5)
    )

    plt.scatter(
        X_scaled[:, numeric_columns.index("MntWines")],
        X_scaled[:, numeric_columns.index("MntMeatProducts")],
        c=labels,
        alpha=0.7
    )

    plt.xlabel(
        "Standardized MntWines"
    )

    plt.ylabel(
        "Standardized MntMeatProducts"
    )

    plt.title(
        "Customer Segmentation using K-Means"
    )

    plt.grid(
        alpha=0.3
    )

    plt.tight_layout()

    plt.show()