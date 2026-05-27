import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# 1. Initialize Inputs and Target
x1, x2 = 0.35, 0.9
target = 0.5
learning_rate = 1.0  # whiteboard par eta (η) 1 assume kiya gaya hai

# 2. Initialize Weights (Whiteboard values)
w13, w23 = 0.1, 0.8
w14, w24 = 0.4, 0.6
w35, w45 = 0.3, 0.9 

# --- FORWARD PASS ---

# Hidden Layer calculation
a1 = (w13 * x1) + (w23 * x2)
y3 = sigmoid(a1)

a2 = (w14 * x1) + (w24 * x2)
y4 = sigmoid(a2)

# Output Layer calculation
a3 = (w35 * y3) + (w45 * y4)
y5 = sigmoid(a3)

epochs = 231

for epoch in range(1, epochs + 1):
    # --- FORWARD PASS ---
    a1 = (w13 * x1) + (w23 * x2)
    y3 = sigmoid(a1)

    a2 = (w14 * x1) + (w24 * x2)
    y4 = sigmoid(a2)

    a3 = (w35 * y3) + (w45 * y4)
    y5 = sigmoid(a3)

    error = target - y5

    # --- BACKWARD PASS ---
    delta5 = sigmoid_derivative(y5) * error
    delta3 = sigmoid_derivative(y3) * (w35 * delta5)
    delta4 = sigmoid_derivative(y4) * (w45 * delta5)

    # --- UPDATE WEIGHTS (in-place) ---
    w35 += (learning_rate * delta5 * y3)
    w45 += (learning_rate * delta5 * y4)

    w13 += (learning_rate * delta3 * x1)
    w23 += (learning_rate * delta3 * x2)
    w14 += (learning_rate * delta4 * x1)
    w24 += (learning_rate * delta4 * x2)

    print(f"Epoch {epoch:2d}: y5={y5:.6f} error={error:.6f}")

print("\nFinal Weights:")
print(f"w35: {w35:.6f}, w45: {w45:.6f}")
print(f"w13: {w13:.6f}, w23: {w23:.6f}")
print(f"w14: {w14:.6f}, w24: {w24:.6f}")