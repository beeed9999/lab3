print("Конвертер валют")
print("1. USD (Доллары) -> RUB (Рубли)")
print("2. RUB (Рубли) -> USD (Доллары)")
print("3. EUR (Евро) -> RUB (Рубли)")
print("4. RUB (Рубли) -> EUR (Евро)")

choice = input("Выберите направление конвертации (1-4): ")

# Задаем курсы валют (вы можете изменить их на актуальные)
USD_RATE = 92.0  # 1 доллар = 92 рубля
EUR_RATE = 100.0 # 1 евро = 100 рублей

if choice == "1":
    amount = float(input("Введите сумму в USD: "))
    print(f"{amount:.2f} USD = {amount * USD_RATE:.2f} RUB")
elif choice == "2":
    amount = float(input("Введите сумму в RUB: "))
    print(f"{amount:.2f} RUB = {amount / USD_RATE:.2f} USD")
elif choice == "3":
    amount = float(input("Введите сумму в EUR: "))
    print(f"{amount:.2f} EUR = {amount * EUR_RATE:.2f} RUB")
elif choice == "4":
    amount = float(input("Введите сумму в RUB: "))
    print(f"{amount:.2f} RUB = {amount / EUR_RATE:.2f} EUR")
else:
    print("Некорректный выбор. Пожалуйста, введите число от 1 до 4.")