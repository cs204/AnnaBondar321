s = input("Приветствие: ")
if s.startswith("здравствуйте"):
    print("$0")
elif s.startswith("з") and not s.startswith("здравствуйте"):
    print("$20")
else:
    print("$100")