from features.shop.menu import Seller

class HurryKart:
    def __init__(self):
        self.running = True
    def show_home(self):
        seller = Seller()
        while self.running:
            print("_____Welcome to HurryKart____")
            print("Who are You?")
            print("1. Customer")
            print("2. Seller")
            choice = input("Enter Your Choice: ")
            if choice == "1":
                print("Welcome Customer")
            elif choice == "2":
                seller.show_menu()
            elif choice == "0":
                exit()
        
if __name__ == "__main__":
    app = HurryKart()
    app.show_home()
