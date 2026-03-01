from features.shop.shop_data import ShopData

class Products:
    def __init__(self):
        self.products = []
        self.shopData = ShopData()
    def create_products(self):
        if not self.shopData.shops:
            print("No Shop Created")
            return
        print("___________________Create Your Shop Products_______________")
        for i, shop in enumerate(self.shopData.shops, start=1):
            print(f"{i}. {shop['name']}")
        while True:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(self.shopData.shops):
                selected_shop = self.shopData.shops[choice - 1]
                break
            else:
                print("Enter correct Choice")

        productName = input("product Name: ")
        price = int(input("Price: "))
        category = input("Category: ")
        product = {
            "name": productName,
            "price": price,
            "category": category,
            "shop": selected_shop
        }
        self.products.append(product)
    def show_products(self):
        if not self.products:
            print("No products yet")
            return
        for i, product in enumerate(self.products, start=1):
            print(f"{i}. Name: {product['name']}, Price: {product['price']}, Category: {product['category']}")