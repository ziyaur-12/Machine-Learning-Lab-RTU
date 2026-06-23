from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np


def main():
	iris = load_iris()
	X = iris.data
	y = iris.target
	feature_names = iris.feature_names

	# Split dataset into train and test sets.
	X_train, X_test, y_train, y_test = train_test_split(
		X, y, test_size=0.3, random_state=42, stratify=y
	)

	# Build and train k-NN model.
	knn = KNeighborsClassifier(n_neighbors=3)
	knn.fit(X_train, y_train)

	y_pred = knn.predict(X_test)

	correct_predictions = []
	wrong_predictions = []

	for i in range(len(y_test)):
		actual_class = iris.target_names[y_test[i]]
		predicted_class = iris.target_names[y_pred[i]]
		row = (
			f"Sample {i + 1:02d} | Features: {X_test[i]} | "
			f"Actual: {actual_class} | Predicted: {predicted_class}"
		)
		if y_test[i] == y_pred[i]:
			correct_predictions.append(row)
		else:
			wrong_predictions.append(row)

	np.set_printoptions(precision=1, suppress=True)
	cm = confusion_matrix(y_test, y_pred)
	report = classification_report(
		y_test,
		y_pred,
		target_names=["0", "1", "2"],
		digits=2,
	)

	print("Output:\n")
	print(" ".join(feature_names))
	print(X_test)
	print("\nclass: 0-Iris-Setosa, 1- Iris-Versicolour, 2- Iris-Virginica")
	print(y_pred)
	print("\nConfusion Matrix")
	print(cm)
	print("\nAccuracy Metrics")
	print(report)

	print(f"Overall Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
	print(f"Correct Predictions: {len(correct_predictions)}")
	print(f"Wrong Predictions: {len(wrong_predictions)}\n")

	print("=== Correct Predictions ===")
	if correct_predictions:
		for item in correct_predictions:
			print(item)
	else:
		print("None")

	print("\n=== Wrong Predictions ===")
	if wrong_predictions:
		for item in wrong_predictions:
			print(item)
	else:
		print("None")


if __name__ == "__main__":
	main()
