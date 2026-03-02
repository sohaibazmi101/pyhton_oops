import random
import math
class Centrality:
    def __init__(self):
        self.data = [(1,2),(2,2),(7,2),(7,2)]
    def _mean(self, data):
        if not self.data:
            print("Empty Data")
            return None
        total = sum(data)
        N = len(data)
        return total / N
    def _median(self, data):
        if not data:
            print("Emty data list")
            return
        _sorted_data = sorted(data)
        N = len(_sorted_data)
        mid = N // 2
        if N % 2 == 0:
            return (_sorted_data[mid - 1] + _sorted_data[mid]) / 2
        else:
            return _sorted_data[mid]
    
    def _mode(self, data):
        counts = {}
        for num in data:
            counts[num] = counts.get(num, 0) + 1
            _max_freq = max(counts.values())
            _modes = []
            for num, count in counts.items():
                if count == _max_freq:
                    _modes.append(num)
        return _modes
    
    def _range(self, data):
        if not data:
            return
        return max(data) - min(data)
    def _quartiles(self, data, _x):
        if not data:
            return
        _sorted_data = sorted(data)
        q2 = self._median(_sorted_data)
        _left_data = []
        _right_data = []
        for i in _sorted_data:
            if i < q2:
                _left_data.append(i)
            elif i > q2:
                _right_data.append(i)
        q1 = self._median(_left_data)
        q3 = self._median(_right_data)
        q0 = min(_sorted_data)
        q4 = max(_sorted_data)
        _iqr = q3 - q1
        _outliers = False
        print("Left Outlier boundary: ",q1 - 1.5 * _iqr)
        print("Right Outlier boundary: ",q3 + 1.5 * _iqr)
        if _x < (q1 - 1.5 * _iqr) or _x > (q3 + 1.5 * _iqr):
            _outliers = True
        return _outliers

    def _variance(self, sample):
        N = len(sample)
        m = self._mean(sample)
        total = 0
        for _ in sample:
            total += self._mean_sqr_distance(_, m)
        return (total) / (N - 1)
    
    def _standard_deviation(self, varince):
        return math.sqrt(varince)

    def _mean_sqr_distance(self, x, m):
        return (x - m) ** 2
    
    def _menu(self):
        _x = []
        _y = []
        for x, y in self.data:
            _x.append(x)
            _y.append(y)
        test_data = []
        _test = [28, 25, 29, 29, 30, 35, 34, 35, 37, 38]
        for i in range(100):
            test_data.append(random.randint(1,90))
        while True:
            print("1. Calculate mean")
            print("2. Calculate Median")
            print("3. Calculate Mode")
            print("4. Range")
            print("5. Variance")
            print("6. Standard Deviation")
            print("7. Quartile")
            print("0. Exit")
            choice = input("Enter Your choice: ")
            if choice == "1":
                mn = self._mean(_x)
                print("Mean: ", mn)
            elif choice == "2":
                me = self._median(_x)
                print("Median: ", me)
            elif choice == "3":
                md = self._mode(_x)
                print(md)
            elif choice == "4":
                print("Range: ", self._range(_x))
            elif choice == "5":
                print("Variance: ", self._variance(_x))
            elif choice == "6":
                var = self._variance(_x)
                print("Standard Deviation: ", self._standard_deviation(var))
            elif choice == "7":
                val = int(input("Enter Value to test on data: "))
                print(self._quartiles(_test, val))
            elif choice == "0":
                print("_____________Exited_______________")
                exit()
            else: 
                print("Please enter correct choice")
if __name__ == "__main__":
    cen = Centrality()
    cen._menu()