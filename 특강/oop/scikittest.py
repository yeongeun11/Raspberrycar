from sklearn.linear_model import SGDRegressor
import numpy as np


np.set_printoptions(suppress=True, precision=2)
X = np.random.rand(3, 1) * 10
# H(x) = w * x + b
y =  np.random.rand(3,1) * 2
y = y.ravel()

# 모델 생성 후 하이퍼파라메터 설정
model = SGDRegressor (
    max_iter=100,
    learning_rate="constant"
    eta0=0.001  
    penalty=None
    random_state=0

)

# 학습 실시
model.fit(X,y)

# 평가
# Loss
y_pred = model.predict(X)



