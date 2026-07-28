# Machine Learning Lab Assignments

This repository contains my Machine Learning laboratory assignments completed as part of my coursework. The assignments cover fundamental concepts of data preprocessing, statistical analysis, similarity measures, matrix operations, and data visualization using Python.

---

## Course Information

- **Course:** Machine Learning 
- **Language:** Python 3

---

## Technologies & Libraries Used

- Python 3
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- OpenPyXL

---

## Repository Structure

```text
ML_lab/
│
├── README.md
├── .gitignore
│
├── questions/
│   ├── Lab01.pdf
│   ├── Lab02.pdf
│   └── Lab03.pdf
│
├── week-1/
│   ├── q1.py
│   ├── q2.py
│   ├── q3.py
│   ├── q4.py
│   └── q5.py
│
├── week-2/
│   ├── A1.py
│   ├── A3.py
│   ├── A4.py
│   ├── A5.py
│   ├── A6.py
│   ├── A7.py
│   ├── A8.py
│   ├── A9.py
│   └── Lab Session Data.xlsx
│
└── week-3/
    ├── A1.py
    ├── A2.py
    ├── A3.py
    ├── A4.py
    ├── A5.py
    ├── A6.py
    ├── A7.py
    ├── A8.py
    ├── A9.py
    ├── A10.py
    └── A11.py
```
---

## Assignments
## week 1 – Python Programming Fundamentals

Introduces fundamental Python programming concepts through modular programming. The assignments involve working with lists, strings, matrices, and basic statistical computations while following structured coding practices.

### week2:-
### A1 – Matrix Operations and Pseudo Inverse
- Loaded data from Excel using Pandas
- Constructed feature matrix (X) and output vector (y)
- Calculated matrix dimensionality
- Determined the rank of the feature matrix
- Computed product costs using the Moore-Penrose Pseudo Inverse

### A2 – Statistical Analysis
- Calculated statistical measures such as mean and variance
- Performed numerical analysis on the given dataset

### A3 – Data Analysis
- Implemented data analysis operations using NumPy and Pandas
- Explored matrix computations and statistical properties

### A4 – Data Exploration
- Identified attribute datatypes
- Suggested suitable encoding techniques
- Examined numeric data ranges
- Detected missing values
- Identified outliers
- Calculated mean and standard deviation for numeric attributes

### A5 – Similarity Measures
- Computed:
  - Jaccard Coefficient (JC)
  - Simple Matching Coefficient (SMC)
- Compared similarity between binary observation vectors

### A6 – Cosine Similarity
- Calculated cosine similarity between observation vectors
- Used complete feature vectors after preprocessing

### A7 – Heatmap Visualization
- Generated similarity matrices using:
  - Jaccard Coefficient
  - Simple Matching Coefficient
  - Cosine Similarity
- Visualized similarity matrices using Seaborn heatmaps

### A8 – Data Imputation
- Filled missing values using:
  - Mean
  - Median
  - Mode
- Selected the appropriate imputation technique based on attribute characteristics

### A9 – Data Normalization
- Applied normalization to numeric attributes
- Used Min-Max Scaling to transform values into a common range

---

### Week 3 – Feature Engineering and Clustering

#### A1 – Feature Datatype Identification
- Identified feature types as Nominal, Ordinal, Interval, or Ratio
- Studied the characteristics of the marketing campaign dataset

#### A2 – Categorical Data Encoding
- Implemented custom Label Encoding
- Implemented custom One-Hot Encoding
- Converted categorical attributes without using built-in encoders

#### A3 – Feature Encoding Analysis
- Applied encoding techniques to categorical features
- Compared dataset dimensionality before and after encoding

#### A4 – Minkowski Distance
- Developed a generalized Minkowski distance function
- Calculated Manhattan and Euclidean distances using different values of p

#### A5 – Distance Analysis
- Computed Minkowski distance for p values from 1 to 10
- Visualized the variation in distance using line plots

#### A6 – Distance Function Validation
- Compared the custom Minkowski distance function with SciPy's implementation
- Verified the correctness of the developed function

#### A7 – Vector Operations
- Implemented custom Dot Product
- Calculated Euclidean Norm of vectors
- Compared results with NumPy functions

#### A8 – Statistical Functions
- Developed custom functions for Mean, Variance, and Standard Deviation
- Computed statistical measures for all numerical features

#### A9 – Comparison with Built-in Functions
- Compared custom statistical functions with NumPy's mean and standard deviation
- Validated the accuracy of the implemented functions

#### A10 – Histogram Analysis
- Generated histograms for selected features
- Studied feature distribution
- Calculated mean and variance for the selected feature

#### A11 – K-Means Clustering
- Implemented the K-Means clustering algorithm from scratch
- Assigned data points to clusters using Euclidean distance
- Updated cluster centroids iteratively until convergence

## Concepts Covered

- Data Exploration
- Data Cleaning
- Missing Value Imputation
- Data Normalization
- Matrix Operations
- Matrix Rank
- Moore-Penrose Pseudo Inverse
- Statistical Analysis
- Similarity Measures
- Cosine Similarity
- Heatmap Visualization
- Feature Engineering
- Data Encoding
- Label Encoding
- One-Hot Encoding
- Feature Engineering
- Distance Metrics
- Minkowski Distance
- Manhattan Distance
- Euclidean Distance
- Vector Operations
- Dot Product
- Euclidean Norm
- Histogram Analysis
- K-Means Clustering

---

## Requirements

Install the required Python libraries using:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
```

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/<your-username>/ML_lab.git
```

2. Navigate to the project directory

```bash
cd ML_lab
```

3. Run any assignment

```bash
python week-2/A1.py
```

---

## Author

**Anushree Kasturi**

B.Tech Computer Science Engineering  
Amrita Vishwa Vidyapeetham, Bengaluru

---