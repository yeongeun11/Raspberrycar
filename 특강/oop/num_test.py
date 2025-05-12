import numpy as np

num_of_samples = 5
num_of_features = 2

# data set
# H(x) = 5X + 3X + 3
np.random.seed(1)
np.set_printoptions(False, suppress=True)
X = np.random.rand(num_of_samples, num_of_features) * 10 # 어떤 차원을 쓸지
x_true = [5, 3]
b_true = 4
noise = np.random.randn(num_of_samples) * 0.5

y = X[:, 0] * 5 + X[:, 1] * 3 + b_true + noise 

print(X)
print(X[:, 0] * 5) # : -> 전부 다 , 모든 행 값을 가져오는 것
print(X[:, 0] * 3)
print(X[:, 0] * 5 + X[:, 1] * 3)