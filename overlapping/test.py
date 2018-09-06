import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([0, 0, 1, 1])
from sklearn.svm import SVC
clf = SVC()
clf.fit(X, y)
