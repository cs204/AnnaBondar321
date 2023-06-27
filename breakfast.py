menu = {"кофе": 20.00,
   "чай": 10.00,
   "булочка": 5.00,
   "салат": 30.40,
   "пирожное": 45.50}

order = []
while True:
    try:
        dish = input("Блюдо: ").lower()
        if dish in menu:
            order.append(menu[dish])
        else:
            print(f"Мы не готовим {dish}, пожалуйста, выберите что-то другое.")
    except EOFError:
        break

sum = sum(order)
print(f"Сумма: {sum:.2f}")

