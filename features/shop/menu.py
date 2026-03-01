from features.shop.shop_data import ShopData
from features.shop.create_product import Products
class Seller:
    def __init__(self):
        self.shopData = ShopData()
        self.products = Products()
    def show_menu(self):
        print("____________Shop Menu_________")
        print("1. Create Shop")
        print("2. Show Shop")
        print("3. Create Products")
        print("4. Show Products")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.shopData.create_shops()
        elif choice == "2":
            self.shopData.show_shops()
        elif choice == "3":
            self.products.create_products()
        elif choice == "4":
            self.products.show_products()
        elif choice == "0":
            exit()
        else:
            print("Enter correct options")
