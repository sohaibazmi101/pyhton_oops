import random
from measures_of_centrality import Centrality
from measure_of_spread import Spread
from plotting import BoxPlot

class App:
    def __init__(self):
        self.data = [28, 25, 29, 29, 30, 35, 34, 35, 37, 38]
        self.centrality = Centrality()
        self.spread = Spread()
        self.plotting = BoxPlot()

    def menu(self):
        # for _ in range(20):
        #     x = random.randint(1,8)
        #     self.data.append(x)
        while True:
            print("______Menu________")
            print("\n1. Calculate Centrality")
            print("2. Calculate Spread")
            print("3. Box Plot")
            print("0. Exit")
            print(self.data)
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.centrality.menu(self.data)
            elif choice == 2:
                self.spread.menu(self.data)
            elif choice == 3:
                self.plotting.menu(self.data)
            elif choice == 0:
                exit()
            else:
                print("Enert correct choice")

if __name__ == "__main__":
    app = App()
    app.menu()