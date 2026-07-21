# Machine Learning Lab Assignments

This repository contains my Machine Learning laboratory assignments completed as part of my coursework. The assignments cover fundamental concepts of data preprocessing, statistical analysis, similarity measures, matrix operations, and data visualization using Python.

---

## Course Information

- **Course:** Machine Learning Lab
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

```
ML_lab/
│
├── week-1/
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
└── README.md
```

---

## Assignments

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