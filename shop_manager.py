import os
import json

filename = "products.json"

def load_products():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    else:
        return {}

def save_products(products):
    with open(filename, "w") as file:
        json.dump(products, file, indent=4)

def list_products(products):
    if not products:
        print("هیچ کالایی در سیستم نیست.")
    else:
        print("\nلیست محصولات:")
        for product, info in products.items():
            print(f"{product} - قیمت: {info['price']} - موجودی: {info['quantity']}")

def add_product(products):
    product_name = input("\nنام محصول را وارد کنید: ")
    if product_name in products:
        print("این محصول قبلاً اضافه شده است.")
    else:
        price = float(input("قیمت محصول را وارد کنید: "))
        quantity = int(input("تعداد موجودی را وارد کنید: "))
        products[product_name] = {"price": price, "quantity": quantity}
        save_products(products)
        print(f"محصول {product_name} اضافه شد.")

def edit_product(products):
    product_name = input("\nنام محصولی که می‌خواهید ویرایش کنید را وارد کنید: ")
    if product_name in products:
        print("1. تغییر قیمت")
        print("2. تغییر موجودی")
        choice = input("انتخاب کنید (1 یا 2): ")
        if choice == "1":
            new_price = float(input("قیمت جدید را وارد کنید: "))
            products[product_name]["price"] = new_price
        elif choice == "2":
            new_quantity = int(input("موجودی جدید را وارد کنید: "))
            products[product_name]["quantity"] = new_quantity
        save_products(products)
        print(f"اطلاعات محصول {product_name} به‌روزرسانی شد.")
    else:
        print("محصول پیدا نشد.")

def delete_product(products):
    product_name = input("\nنام محصولی که می‌خواهید حذف کنید را وارد کنید: ")
    if product_name in products:
        del products[product_name]
        save_products(products)
        print(f"محصول {product_name} حذف شد.")
    else:
        print("محصول پیدا نشد.")

def main():
    products = load_products()
    
    while True:
        print("\n--- منوی مدیریت مغازه ---")
        print("1. نمایش لیست محصولات")
        print("2. اضافه کردن محصول")
        print("3. ویرایش محصول")
        print("4. حذف محصول")
        print("5. خروج")
        choice = input("انتخاب کنید: ")
        
        if choice == "1":
            list_products(products)
        elif choice == "2":
            add_product(products)
        elif choice == "3":
            edit_product(products)
        elif choice == "4":
            delete_product(products)
        elif choice == "5":
            break
        else:
            print("انتخاب نامعتبر. دوباره امتحان کنید.")

if __name__ == "__main__":
    main()
def search_product(products):
    product_name = input("\nنام محصولی که می‌خواهید جستجو کنید را وارد کنید: ")
    if product_name in products:
        print(f"{product_name} - قیمت: {products[product_name]['price']} - موجودی: {products[product_name]['quantity']}")
    else:
        print("محصول پیدا نشد.")

def main():
    products = load_products()
    
    while True:
        print("\n--- منوی مدیریت مغازه ---")
        print("1. نمایش لیست محصولات")
        print("2. اضافه کردن محصول")
        print("3. ویرایش محصول")
        print("4. حذف محصول")
        print("5. جستجو در محصولات")  # اضافه کردن گزینه جستجو
        print("6. خروج")
        choice = input("انتخاب کنید: ")
        
        if choice == "1":
            list_products(products)
        elif choice == "2":
            add_product(products)
        elif choice == "3":
            edit_product(products)
        elif choice == "4":
            delete_product(products)
        elif choice == "5":
            search_product(products)  # افزودن عملکرد جستجو
        elif choice == "6":
            break
        else:
            print("انتخاب نامعتبر. دوباره امتحان کنید.")
