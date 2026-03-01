class ShopData:
    def __init__(self):
        self.shops = []
    def create_shops(self):
        print("_______create Your Shop__________")
        name = input("Enter Your shop name: ")
        address = input("Enter Your Shop Address: ")
        category = input("Enert Shop Category: ")
        shop = {
            "name": name,
            "address": address,
            "category": category
        }
        self.shops.append(shop)
        print("Shop Created Sucessfully")
        print(f"Shop {shop}")
    def show_shops(self):
        if not self.shops:
            print("No shop Created")
            return
        for i, shop in enumerate(self.shops, start=1):
            print(f"{i}. Name: {shop['name']}, Address: {shop['address']}, Category: {shop['category']}")