import random

data = []

for _ in range(100):
    x1 = random.randint(1, 20)
    x2 = random.randint(1, 20)
    z = 2*x1 + 3*x2
    data.append(([x1, x2], z))

W = [random.random(), random.random()]
b = random.random()

lr = 0.00001

def relu(x):
    return max(0, x)

def relu_derivative(x):
    if x > 0:
        return 1
    else:
        return 0

for epoch in range(1000):
    total_loss = 0

    for X, z in data:

        linear_output = sum(W[i]*X[i] for i in range(len(W))) + b

        z_pred = relu(linear_output)

        loss = (z_pred - z) ** 2
        total_loss += loss

        dloss = 2 * (z_pred - z)

        drelu = relu_derivative(linear_output)

        for i in range(len(W)):
            dW = dloss * drelu * X[i]
            W[i] -= lr * dW

        db = dloss * drelu
        b -= lr * db

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss {total_loss}")

print("\nLearned W:", W)
print("Learned b:", b)

print("\nTesting:")
test_X = [3, 2]
linear = sum(W[i]*test_X[i] for i in range(len(W))) + b
prediction = relu(linear)
print("Prediction:", prediction)