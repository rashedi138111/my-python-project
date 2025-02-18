import os
import json

# فایل برای ذخیره اطلاعات محصولات
filename = "products.json"

# بارگذاری محصولات از فایل
def load_products():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    else:
        return {}

# ذخیره محصولات در فایل
def save_products(products):
    with open(filename, "w") as file:
        json.dump(products, file, indent=4)

# نمایش لیست محصولات
def list_products(products):
    if not products:
        print("هیچ کالایی در سیستم نیست.")
    else:
        print("\nلیست محصولات:")
        for product, info in products.items():
            print(f"{product} - قیمت: {info['price']} - موجودی: {info['quantity']}")

# اضافه کردن محصول جدید
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

# ویرایش اطلاعات محصول
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

# حذف محصول
def delete_product(products):
    product_name = input("\nنام محصولی که می‌خواهید حذف کنید را وارد کنید: ")
    if product_name in products:
        del products[product_name]
        save_products(products)
        print(f"محصول {product_name} حذف شد.")
    else:
        print("محصول پیدا نشد.")

# منوی اصلی
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

