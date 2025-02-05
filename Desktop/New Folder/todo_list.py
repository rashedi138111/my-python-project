# ایجاد یک لیست خالی برای ذخیره کارها
tasks = [‎‎‎‎‎

# نمایش پیامی برای شروع
print("لیست کارهای روزمره")

# حلقه برای اضافه کردن کارها به لیست
while True:
    task = input("یک کار جدید وارد کنید (برای تمام کردن 'خروج' را بنویسید): ")
    if task.lower() == 'خروج':
        break
    tasks.append(task)

# نمایش لیست تمام کارهای وارد شده
print("\nلیست تمام کارهای شما:")
for index, task in enumerate(tasks, 1):
    print(f"{index}. {task}")
