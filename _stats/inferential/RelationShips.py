import math
import random

class Relations:
    def __init__(self):
        self.data = []
    
    def _mean(self, data):
        return sum(data) / len(data)
    
    def _mean_diff(self, _x, mean):
        return _x - mean
    
    def _product_of_diff(self, _x, _y):
        return _x * _y
    
    def _mean_sqr_dist(self, x, mean):
        return (x - mean) ** 2
    
    def _variance(self, sample):
        N = len(sample)
        _total = 0
        m = self._mean(sample)
        for i in sample:
            _total += self._mean_sqr_dist(i, m)
        return _total / (N - 1)
    
    def _std_deviation(self, _var):
        return math.sqrt(_var)
    
    def _covariance(self, data):
        _x_data = []
        _y_data = []
        for x, y in data:
            _x_data.append(x)
            _y_data.append(y)
        _x_mean = self._mean(_x_data)
        _y_mean = self._mean(_y_data)
        _sum_of_product_of_mean_diff = 0
        for x, y in data:
            _x_mean_diff = self._mean_diff(x, _x_mean)
            _y_mean_diff = self._mean_diff(y, _y_mean)
            _sum_of_product_of_mean_diff += self._product_of_diff(_x_mean_diff, _y_mean_diff)
        return _sum_of_product_of_mean_diff / (len(data) - 1)
    
    def _linear_regression(self, data, _x):
        _x_data = []
        _y_data = []
        for x, y in data:
            _x_data.append(x)
            _y_data.append(y)
        _m = self._covariance(data) / self._variance(_x_data)
        _y_mean = self._mean(_y_data)
        _x_mean = self._mean(_x_data)
        _b = _y_mean - _m * _x_mean
        return _m * _x + _b
    
    def _correlation(self, data):
        _x_data = []
        _y_data = []
        for x, y in data:
            _x_data.append(x)
            _y_data.append(y)
        _cov = self._covariance(data)
        _x_var = self._variance(_x_data)
        _y_var = self._variance(_y_data)
        _x_std_deviation = self._std_deviation(_x_var)
        _y_std_deviation = self._std_deviation(_y_var)
        return _cov / (_x_std_deviation * _y_std_deviation)

    
    def _menu(self):
        self.data = []
        for i in range(100):
            _x = random.randint(1,20)
            _y = random.randint(71,90)
            self.data.append((_x, _y))
        test_data = [(1,2),(2,4),(3,6),(4,8)]
        cov = self._covariance(self.data)
        print("Covariance: ", cov)
        corr = self._correlation(self.data)
        print("Correlation: ", corr)
        print("Y Prediction of X = 10: ", self._linear_regression(self.data, 10))
    
if __name__ == "__main__":
    rel = Relations()
    rel._menu()
