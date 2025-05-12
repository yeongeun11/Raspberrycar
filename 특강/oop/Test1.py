
samples = []
y = []

w = [0.2, 0.3]
b = 0.1

gradient_w = [0.0, 0.0]
gradient_b = 0.0

# 1 
for dp, y_ in zip(samples, y):
    # 예측값
    predict_y = w[0] * dp[0] + w[1] * dp[1] + b 

    # 오차 : 예측값 - 정답
    error = predict_y 

    # 기울기 값 누적
    gradient_w[0] += dp[0] * error
    gradient_w[1] += dp[1] * error
    gradient_b += error

# update gradient of each W
gradient_w[0] = - gradient_w[0] / len(samples)
gradient_w[1] = - gradient_w[1] / len(samples)

# update gradient of b 
b = b -  gradient_b