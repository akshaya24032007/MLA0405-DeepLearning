import numpy as np

np.random.seed(1)

dimensions = [2,5,10,20]

for d in dimensions:
    p1 = np.random.rand(d)
    p2 = np.random.rand(d)

    distance = np.linalg.norm(p1-p2)

    print("Dimension:", d)
    print("Distance:", round(distance,3))
    print()
