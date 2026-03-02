from measures_of_centrality import Centrality

class BoxPlot:
    def __init__(self):
        self.centrality = Centrality()

    def box_plot(self, data):
        sorted_data = sorted(data)
        median = self.centrality.median(data)
        q1_data = [num for num in sorted_data if num < median]
        q1 = self.centrality.median(q1_data)
        q3_data = [num for num in sorted_data if num > median]
        q3 = self.centrality.median(q3_data)
        q0 = min(sorted_data)
        q4 = max(sorted_data)
        iqr = q3 - q1
        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)
        return [lower_bound, upper_bound]
    
    def menu(self, data):
        while True:
            print("1. box plot")
            print("0. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                bp = self.box_plot(data)
                print("Box Plot: ", bp)
            elif choice == 0:
                return
            else:
                print("Enter correct choice")