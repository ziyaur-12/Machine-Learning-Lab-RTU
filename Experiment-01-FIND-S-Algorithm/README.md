# Experiment 1 - FIND-S Algorithm in Machine Learning (RTU)

## Aim
 Implement and demonstrate the FIND-Salgorithm for finding the most specific 
hypothesis based on a given set of training data samples. Read the training 
data from a .CSV file. 
---

## Introduction
FIND-S algorithm is a concept learning algorithm in Machine Learning. It finds the most specific hypothesis that fits all positive training examples. It ignores negative examples and gradually generalizes the hypothesis.

---

## Algorithm Steps
1. Initialize hypothesis to the most specific (all attributes set to null).
2. For each training example:
   - If the example is positive:
     - Compare it with the current hypothesis.
     - Update the hypothesis:
       - If attribute is null → replace with value.
       - If values differ → replace with '?'.
   - If the example is negative:
     - Ignore it.
3. Output the final hypothesis.

---

## Dataset
The training data is provided in a CSV file:

**File:** `Training_Data.csv`

### Sample Data:

| Sky   | AirTemp | Humidity | Wind   | Water | Forecast | EnjoySport |
|------|--------|----------|--------|--------|----------|------------|
| Sunny | Warm | Normal | Strong | Warm | Same | Yes |
| Sunny | Warm | High | Strong | Warm | Same | Yes |
| Rainy | Cold | High | Strong | Warm | Change | No |
| Sunny | Warm | High | Strong | Cool | Change | Yes |

---

## Code Explanation
- The program reads data using `pandas`.
- It initializes the hypothesis as the most specific.
- Iterates through each training example.
- Updates hypothesis only for positive examples.
- Prints intermediate and final hypothesis.

---

## Implementation

```python
import pandas as pd

def find_s_algorithm(csv_file):
    data = pd.read_csv(csv_file)

    attributes = data.columns[:-1]
    target = data.columns[-1]

    hypothesis = ['0'] * len(attributes)

    print("Initial Hypothesis:", hypothesis)

    for index, row in data.iterrows():
        if row[target] == 'Yes':
            print(f"\nProcessing positive example {index + 1}:")
            print(list(row[attributes]))

            for i in range(len(hypothesis)):
                if hypothesis[i] == '0':
                    hypothesis[i] = row[attributes[i]]
                elif hypothesis[i] != row[attributes[i]]:
                    hypothesis[i] = '?'

            print("Updated Hypothesis:", hypothesis)

    return hypothesis


if __name__ == "__main__":
    final_hypothesis = find_s_algorithm("Training_Data.csv")

    print("\nFinal Most Specific Hypothesis:")
    print(final_hypothesis)
