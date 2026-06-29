# Experiment 10 - Locally Weighted Regression (LWR)

## Aim

To implement the Non-Parametric Locally Weighted Regression (LWR) algorithm for fitting data points and visualize the fitted regression curve using graphs.

---

## Objective

To understand how Locally Weighted Regression performs nonlinear regression by assigning higher weights to nearby data points and lower weights to distant points.

---

## Introduction

Locally Weighted Regression (LWR), also known as LOESS or LOWESS, is a non-parametric machine learning algorithm used for regression analysis.

Unlike Linear Regression, LWR does not learn one global model. Instead, it builds a local regression model for every query point using nearby training samples.

---

## Theory

The prediction for each query point is obtained by fitting a weighted linear regression model.

The weight assigned to each training sample is calculated using the Gaussian Kernel:

\[
w(i)=\exp\left(-\frac{(x_i-x)^2}{2\tau^2}\right)
\]

Where:

- **x** = Query point
- **xi** = Training sample
- **τ (tau)** = Bandwidth parameter
- **w(i)** = Weight assigned to training sample

Nearby points receive higher weights while distant points receive lower weights.

---

## Dataset

**Dataset File**

```text
data.csv
```

The dataset contains sample input-output values used to train and test the Locally Weighted Regression model.

---

## Files Included

- **ml_exp10.py** – Python implementation of Locally Weighted Regression
- **data.csv** – Dataset used for regression
- **output_1.png** – Scatter plot of dataset
- **output_2.png** – Regression curve generated using LWR
- **README.md** – Project documentation

---

## Requirements

Install the required Python libraries:

```bash
pip install numpy pandas matplotlib scikit-learn
```

---

## How to Run

Execute the program using:

```bash
python ml_exp10.py
```

---

## Output

The program performs the following tasks:

- Reads the dataset
- Fits the Locally Weighted Regression model
- Predicts output values
- Draws the original data points
- Draws the fitted regression curve

---

## Applications

- Weather Prediction
- Financial Forecasting
- Stock Price Analysis
- Sales Prediction
- Medical Data Analysis
- Nonlinear Regression Problems

---

## Advantages

- Handles nonlinear relationships effectively
- Smooth regression curve
- No global model assumption
- Flexible and accurate for local predictions

---

## Limitations

- Computationally expensive
- Slow for large datasets
- Requires selecting an appropriate bandwidth parameter

---

## Result

The Non-Parametric Locally Weighted Regression algorithm was successfully implemented. The regression model accurately fitted the data points and generated a smooth regression curve illustrating local trends in the dataset.

---

## Keywords

Machine Learning, Locally Weighted Regression, LWR, LOESS, LOWESS, Regression, Non-Parametric Learning, Python, RTU Lab Experiment