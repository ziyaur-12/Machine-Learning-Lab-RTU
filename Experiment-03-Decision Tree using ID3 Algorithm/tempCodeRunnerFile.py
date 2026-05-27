import pandas as pd
import math
from pathlib import Path

# Load dataset from CSV file
data_path = Path(__file__).resolve().parent / "play_tennis.csv"
data = pd.read_csv(data_path)

# Entropy calculation
def entropy(column):
    values = column.value_counts()
    total = len(column)
    ent = 0
    for count in values:
        p = count / total
        ent -= p * math.log2(p)
    return ent

# Information Gain calculation
def information_gain(data, feature, target):
    total_entropy = entropy(data[target])
    weighted_entropy = 0

    for value in data[feature].unique():
        subset = data[data[feature] == value]
        weighted_entropy += (len(subset) / len(data)) * entropy(subset[target])

    return total_entropy - weighted_entropy

# ID3 Algorithm
def id3(data, features, target):
    # If all outputs are same
    if len(data[target].unique()) == 1:
        return data[target].iloc[0]

    # If no features left
    if len(features) == 0:
        return data[target].mode()[0]

    # Choose best feature
    gains = {f: information_gain(data, f, target) for f in features}
    best_feature = max(gains, key=gains.get)

    tree = {best_feature: {}}
    remaining_features = [f for f in features if f != best_feature]

    for value in data[best_feature].unique():
        subset = data[data[best_feature] == value]
        tree[best_feature][value] = id3(subset, remaining_features, target)

    return tree

# Classification function
def classify(tree, sample):
    if not isinstance(tree, dict):
        return tree

    feature = next(iter(tree))
    value = sample[feature]

    return classify(tree[feature][value], sample)

# Main execution
features = ["outlook", "temperature", "humidity", "wind"]
target = "answer"

decision_tree = id3(data, features, target)
print("Decision Tree:")
print(decision_tree)

# New sample classification
new_sample = {
    "outlook": "sunny",
    "temperature": "cool",
    "humidity": "high",
    "wind": "strong"
}

prediction = classify(decision_tree, new_sample)
print("\nNew Sample:", new_sample)
print("Predicted Class:", prediction)
