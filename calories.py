fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 76,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineappl": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelone": 80,
}

fruit = input("Фрукт: ").lower()

if fruit in fruits:
    calories = fruits[fruit]
    print(f"Калории: {calories}")
else:
    print("Калорийная информация для этого фрукта не доступна.")