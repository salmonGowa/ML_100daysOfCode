from sklearn.datasets import make_circles
import matplotlib.pyplot as plt

X, y = make_circles(n_samples=200, shuffle=True, noise=0.1, random_state=42)
# Plot the generated datasets
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()