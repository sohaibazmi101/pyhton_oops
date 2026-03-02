import random

data = [
    (1,4),
    (2,8),
    (3,12)
]

w = random.random()
b = random.random()

lr = 0.01

for epoch in range(1000):
    total_loss = 0
    for x, y in data:
        y_pred = w * x + b
        loss = (y_pred - y) ** 2
        total_loss += loss
        dw = 2 * (y_pred - y) * x
        db = 2 * (y_pred - y)
        w -= lr * dw
        b -= lr * db
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss {total_loss}")

print("Final Learned valued")
print("w: ", w)
print("b: ", b)
print("\nTesting: ")
print("x = 2 ", 4 * w + b)