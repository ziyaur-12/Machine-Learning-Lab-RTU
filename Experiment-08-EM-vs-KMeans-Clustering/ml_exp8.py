import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.metrics as sm
from sklearn import datasets, preprocessing
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture


def main() -> None:
	iris = datasets.load_iris()

	x = pd.DataFrame(
		iris.data,
		columns=["Sepal_Length", "Sepal_Width", "Petal_Length", "Petal_Width"],
	)
	y = pd.Series(iris.target, name="Targets")

	kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
	kmeans.fit(x)

	plt.figure(figsize=(14, 7))
	colormap = np.array(["red", "lime", "black"])

	# Plot the original classifications.
	plt.subplot(1, 2, 1)
	plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y.values], s=40)
	plt.title("Real Classification")
	plt.xlabel("Petal Length")
	plt.ylabel("Petal Width")

	# Plot KMeans classifications.
	plt.subplot(1, 2, 2)
	plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[kmeans.labels_], s=40)
	plt.title("KMeans Classification")
	plt.xlabel("Petal Length")
	plt.ylabel("Petal Width")

	print("The accuracy score of KMeans:")
	print(sm.accuracy_score(y, kmeans.labels_))
	print("The confusion matrix of KMeans:")
	print(sm.confusion_matrix(y, kmeans.labels_))

	scaler = preprocessing.StandardScaler()
	x_scaled = scaler.fit_transform(x)

	gmm = GaussianMixture(n_components=3, random_state=42)
	gmm.fit(x_scaled)
	y_gmm = gmm.predict(x_scaled)

	plt.figure(figsize=(7, 5))
	plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y_gmm], s=40)
	plt.title("GMM Classification")
	plt.xlabel("Petal Length")
	plt.ylabel("Petal Width")

	print("The accuracy score of EM (GMM):")
	print(sm.accuracy_score(y, y_gmm))
	print("The confusion matrix of EM (GMM):")
	print(sm.confusion_matrix(y, y_gmm))

	plt.show()


if __name__ == "__main__":
	main()