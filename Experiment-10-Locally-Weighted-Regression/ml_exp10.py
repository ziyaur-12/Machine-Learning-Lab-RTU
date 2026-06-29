import numpy as np
import matplotlib.pyplot as plt


def target_function(x):
    # W-shaped function for LWLR visualization.
    return np.abs(x) - 1.0 / (np.abs(x) + 0.25)


def lwlr_predict(x_query, x_train, y_train, tau):
    x_design = np.column_stack((np.ones_like(x_train), x_train))
    xq = np.array([1.0, x_query])

    diff = x_train - x_query
    weights = np.exp(-(diff ** 2) / (2.0 * tau ** 2))
    w_diag = np.diag(weights)

    xtwx = x_design.T @ w_diag @ x_design
    theta = np.linalg.pinv(xtwx) @ x_design.T @ w_diag @ y_train
    return float(xq @ theta)


def lwlr_curve(x_train, y_train, tau):
    return np.array([lwlr_predict(x, x_train, y_train, tau) for x in x_train])


def main():
    np.random.seed(7)

    n_samples = 1000
    x = np.linspace(-3.0, 3.0, n_samples)
    y_true = target_function(x)
    y_noisy = y_true + np.random.normal(0.0, 0.08, size=n_samples)

    tau_values = [10, 1, 0.1, 0.01]

    fig, axes = plt.subplots(2, 2, figsize=(9, 10))
    for ax, tau in zip(axes.ravel(), tau_values):
        y_pred = lwlr_curve(x, y_noisy, tau)
        ax.scatter(x, y_noisy, s=10, alpha=0.35, color="#3B7CC6")
        ax.plot(x, y_pred, color="red", linewidth=1.8)
        ax.set_title(f"tau={tau}")
        ax.grid(True, alpha=0.25)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()