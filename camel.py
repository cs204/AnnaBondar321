input_var = input("Верблюжий стиль: ")
snake_var = ""

for char in input_var:
    if char.isupper():
        snake_var += "_" + char.lower()
    else:
        snake_var += char

print(snake_var)