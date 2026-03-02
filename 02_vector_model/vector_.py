import random

data = []

for _ in range(100):
    x1 = random.randint(1, 20)
    x2 = random.randint(1, 20)
    z = 2*x1 + 3*x2
    data.append(([x1, x2], z))

W = [random.random(), random.random()]
b = random.random()
lr = 0.0001

for epoch in range(1000):
    total_loss = 0

    for X, z in data:
        z_pred = 0
        for i in range(len(W)):
            z_pred += W[i] * X[i]
        z_pred += b
        loss = (z_pred - z) ** 2
        total_loss += loss
        for i in range(len(W)):
            dw = 2 * (z_pred - z) * X[i]
            W[i] -= lr * dw
        db = 2 * (z_pred - z)
        b -= lr * db
    if epoch % 100 == 0:
        print(f"Epoch: {epoch}, Loss: {total_loss}")

print("Learned W:", W)
print("LEarned b", b)

print("___________________Testing________________")
test_X = [3,2]
z_test = sum(W[i] * test_X[i] for i in range(len(W))) + b

print("Prediction for [3,2]: ", z_test)
