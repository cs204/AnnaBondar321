def calculate_fuel_percentage(fraction):
    try:
        x, y = map(int, fraction.split('/'))

        if x > y or y == 0:
            raise ValueError

        percentage = x / y * 100

        if percentage <= 1:
            return "E"

        if percentage >= 99:
            return "F"

        return round(percentage)

    except ValueError:
        print("Ошибка ввода. Попробуйте еще раз.")

    except ZeroDivisionError:
        print("Деление на ноль. Попробуйте еще раз.")

fraction = input("Дробь: ")

fuel_percentage = calculate_fuel_percentage(fraction)

print(f"Топлива в баке: {fuel_percentage}%")

