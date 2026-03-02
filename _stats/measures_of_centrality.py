class Centrality:
    def mean(self, data):
        if not data:
            return None
        return sum(data)/len(data)
    def median(self, data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid])/2
        else:
            return sorted_data[mid]
    def mode(self, data):
        counts = {}
        for num in data:
            counts[num] = counts.get(num, 0) + 1
        max_freq = max(counts.values())
        _mode = []
        for num, count in counts.items():
            if count == max_freq:
                _mode.append(num)
        return _mode
    def menu(self, data):
        while True:
            print("______Menu________")
            print("\n1. Calculate mean")
            print("2. Calculate Median")
            print("3. Mode")
            print("0. Exit")
            choice = int(input("Enert your choice: "))
            if choice == 1:
                mean = self.mean(data)
                print("Mean: ", mean)
            elif choice == 2:
                median = self.median(data)
                print("Median: ", median)
            elif choice == 3:
                mode = self.mode(data)
                print("Mode: ", mode)
            elif choice == 0:
                return
            else:
                print("Enert correct choice")