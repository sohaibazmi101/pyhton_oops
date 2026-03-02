class Regression:
    def __init__(self):
        pass

    def fit(self, data, x_value):
        _x_data = []
        _y_data = []
        _sum_xy = 0
        _sum_x_sqr = 0
        N = len(data)
        for x, y in data:
            _x_data.append(x)
            _y_data.append(y)
            _sum_xy += (x * y)
            _sum_x_sqr += (x ** 2)
        _sum_x = sum(_x_data)
        _sum_y = sum(_y_data)
        m = (N * _sum_xy - _sum_x * _sum_y) / (N * _sum_x_sqr - (_sum_x ** 2))
        c = (_sum_y - m * _sum_x) / N
        return m * x_value + c
    def menu(self, data):
        while True:
            print("1. Predict y")
            print("0. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                x = int(input("Enter value of x: "))
                y = self.fit(data, x)
                print("y: ", y)
            elif choice == 0:
                return
            else:
                print("Enter correct choice")