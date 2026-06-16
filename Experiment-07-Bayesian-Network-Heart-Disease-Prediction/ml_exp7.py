import numpy as np
import pandas as pd
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

# pgmpy 0.1.x expects np.product, removed in newer numpy.
if not hasattr(np, "product"):
	np.product = np.prod

try:
	# Newer pgmpy versions
	from pgmpy.models import BayesianNetwork as BayesianModel
except ImportError:
	# Older pgmpy versions
	from pgmpy.models import BayesianModel


def main() -> None:
	# Read Cleveland Heart Disease data
	heart_disease = pd.read_csv("heart.csv")
	heart_disease = heart_disease.replace("?", np.nan)

	# Display dataset preview and dtypes
	print("Sample instances from the dataset are given below")
	print(heart_disease.head())
	print("\nAttributes and datatypes")
	print(heart_disease.dtypes)

	# Create Bayesian Network
	model = BayesianModel(
		[
			("age", "heartdisease"),
			("sex", "heartdisease"),
			("exang", "heartdisease"),
			("cp", "heartdisease"),
			("heartdisease", "restecg"),
			("heartdisease", "chol"), 1

			
		]
	)

	# Learn CPDs using Maximum Likelihood Estimator
	print("\nLearning CPD using Maximum Likelihood Estimator")
	model.fit(heart_disease, estimator=MaximumLikelihoodEstimator)

	# Inferencing with Bayesian Network
	print("\nInferencing with Bayesian Network:")
	infer = VariableElimination(model)

	# Compute P(heartdisease | restecg=1)
	print("\n1. Probability of heartdisease given evidence restecg=1")
	q1 = infer.query(variables=["heartdisease"], evidence={"restecg": 1})
	print(q1)

	# Compute P(heartdisease | cp=2)
	print("\n2. Probability of heartdisease given evidence cp=2")
	q2 = infer.query(variables=["heartdisease"], evidence={"cp": 2})
	print(q2)


if __name__ == "__main__":
	main()