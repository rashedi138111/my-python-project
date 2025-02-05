import os

FILENAME = "todo.txt"

todo_list = []

def load_tasks():
    """خواندن لیست کارها از فایل هنگام اجرای برنامه"""
    global todo_list
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as file:
            todo_list = file.read().splitlines()

def save_tasks():
    """ذخیره لیست کارها در فایل"""
    with open(FILENAME, "w", encoding="utf-8") as file:
        for task in todo_list:
            file.write(task + "\n")

def show_list():
    """نمایش تمام کارهای موجود در لیست"""
    if len(todo_list) == 0:
        print("لیست کارها خالی است.")
    else:
        print("\nلیست کارها:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def add_task(task):
    """اضافه کردن یک کار جدید به لیست"""
    todo_list.append(task)
    save_tasks()
    print(f"کار '{task}' به لیست اضافه شد.")

def remove_task(index):
    """حذف یک کار از لیست با استفاده از ایندکس"""
    try:
        removed_task = todo_list.pop(index - 1)
        save_tasks()
        print(f"کار '{removed_task}' از لیست حذف شد.")
    except IndexError:
        print("ایندکس وارد شده اشتباه است.")

def main():
    """منو و ورودی کاربر"""
    load_tasks()
    while True:
        print("\nمنو:")
        print("1. نمایش لیست کارها")
        print("2. اضافه کردن کار جدید")
        print("3. حذف کردن کار")
        print("4. خروج")
        
        choice = input("لطفاً یک شماره وارد کنید: ")

        if choice == "1":
            show_list()
        elif choice == "2":
            task = input("نام کار جدید را وارد کنید: ")
            add_task(task)
        elif choice == "3":
            show_list()
            try:
                index = int(input("شماره کار مورد نظر برای حذف را وارد کنید: "))
                remove_task(index)
            except ValueError:
                print("لطفاً یک عدد وارد کنید.")
        elif choice == "4":
            print("لیست ذخیره شد. خداحافظ!")
            break
        else:
            print("انتخاب نامعتبر. لطفاً یک گزینه درست وارد کنید.")

if _name_ == "_main_":
    main()
