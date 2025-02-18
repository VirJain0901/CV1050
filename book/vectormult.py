import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_vectors(vectors, colors, labels):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])
    
    for vec, color, label in zip(vectors, colors, labels):
        ax.quiver(0, 0, 0, vec[0], vec[1], vec[2], color=color, label=label)
    
    ax.legend()
    plt.show()

# Define two vectors
a = np.array([0.5, 0.2, 0.7])
b = np.array([0.3, 0.8, 0.4])

# Compute dot product
dot_product = np.dot(a, b)
print(f"Dot Product: {dot_product}")

# Compute cross product
cross_product = np.cross(a, b)
print(f"Cross Product: {cross_product}")

# Plot vectors and cross product
plot_vectors([a, b, cross_product], ['r', 'g', 'b'], ['Vector A', 'Vector B', 'Cross Product'])
