# 🌳 Experiment 03 - Decision Tree using ID3 Algorithm

## 📌 Aim

Write a program to demonstrate the working of the decision tree based ID3 
algorithm. Use an appropriate data set for building the decision tree and apply 
this knowledge toclassify a new sample 
---

# 📘 Theory

Decision Tree is a supervised machine learning algorithm used for classification and prediction tasks.

The ID3 (Iterative Dichotomiser 3) algorithm constructs a decision tree using:

- Entropy
- Information Gain

The feature with the highest Information Gain becomes the root node of the tree.

---

# 📊 Dataset Used

Play Tennis Dataset

| Outlook | Temperature | Humidity | Wind | Answer |
|----------|-------------|-----------|------|---------|
| sunny | hot | high | weak | no |
| sunny | hot | high | strong | no |
| overcast | hot | high | weak | yes |
| rain | mild | high | weak | yes |

---

# 🛠 Technologies Used

- Python
- Pandas
- Math Module

---

# 📂 Project Structure

```bash
Experiment-03-Decision Tree using ID3 Algorithm/
│
├── decision_tree_id3.py
├── play_tennis.csv
├── output.png
└── README.md
