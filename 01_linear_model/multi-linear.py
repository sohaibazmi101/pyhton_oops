import random

data = [
    (1,1,4),
    (2,2,5),
    (3,3,6),
    (4,2,3)
]

w1 = random.random()

w2 = random.random()

b = random.random()

lr = 0.02

for epoch in range(1000):
    total_loss = 0
    for x,y,z in data:
        z_pred = w1 * x + w2 * y + b
        loss = (z_pred - z) ** 2
        total_loss += loss
        dw1 = 2 * (z_pred - z) * x
        dw2 = 2 * (z_pred - z) * y
        db = 2 * (z_pred - z)
        w1 -= lr * dw1
        w2 -= lr * dw2
        b -= lr * db
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {total_loss}")

print("Pridicted value->")
print("w1: ",w1)
print("w2: ",w2)
print("b: ",b)
print("\nTesting: ")
print("x = 2, y = 8 -> ", 2 * w1 + 8 * w2 + b)