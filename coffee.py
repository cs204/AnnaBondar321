amount_due = 50
balance = 0

while True:
    coin = int(input("Вставьте монетку: "))
    if coin not in [5, 10, 20, 50]:
        print("Кофе стоит 50 рублей. Принимаются монеты достоинством 5, 10, 20 и 50 рублей.")
        continue

    balance += coin
    print(f"Нужная сумма: {amount_due - balance}")

    if balance >= amount_due:
        change_owed = balance - amount_due
        print(f"Ваша сдача: {change_owed}")
        break