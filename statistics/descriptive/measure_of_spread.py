from measures_of_centrality import Centrality
import math
class Spread:
    def __init__(self):
        self.centrality = Centrality()
    
    def variance(self, data):
        mean = self.centrality.mean(data)
        N = len(data)
        total = 0
        for i in range(N):
            total += self.square_diff(data[i], mean)
        return total / (N-1)

    def square_diff(self, x, mean):
        difference = x - mean
        return difference ** 2
    
    def standard_deviation(self, data):
        v = self.variance(data)
        return math.sqrt(v)
    
    def menu(self, data):
        while True:
            print("\n1. Variance")
            print("2. Standard Deviation")
            print("0. Exit")
            choice = int(input("____Enter Your Choice______"))
            if choice == 1:
                v = self.variance(data)
                print("Varince: ", v)
            elif choice == 2:
                sd = self.standard_deviation(data)
                print("Standard Deviation: ", sd)
            elif choice == 0:
                return
            else:
                print("Enter correct input")