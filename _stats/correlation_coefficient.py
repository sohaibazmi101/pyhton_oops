from measures_of_centrality import Centrality
import math

class Correlation:
    def __init__(self):
        self.centrality = Centrality()

    def _correlation_coefficient(self, data):
        _x_data = []
        _y_data = []
        for x, y in data:
            _x_data.append(x)
            _y_data.append(y)
        _x_mean = self.centrality.mean(_x_data)
        _y_mean = self.centrality.mean(_y_data)
        _x_diff = 0
        _y_diff = 0
        _x_y_total = 0
        for x, y in data:
            _x_y_total += (self._mean_diff(x, _x_mean) * self._mean_diff(y, _y_mean))

            _x_diff += self._mean_diff_sqr(self._mean_diff(x, _x_mean))
            _y_diff += self._mean_diff_sqr(self._mean_diff(y, _y_mean))
        r = _x_y_total / math.sqrt(_x_diff * _y_diff)
        return r
        
    
    def _mean_diff(self, x, mean):
        return x - mean
    def _mean_diff_sqr(self, value):
        return value ** 2
    
    def menu(self, data):
        while True:
            print("1. Correlation Coeficients")
            print("0. Exit")
            choice = int(input("Enert your choice: "))
            if choice == 1:
                r = self._correlation_coefficient(data)
                print("Correlation Coefficient: ", r)
            elif choice == 0:
                return
            else:
                print("Enter correct choice")