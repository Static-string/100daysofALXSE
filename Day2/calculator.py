first_arg, sec_arg, third_arg = input("Enter the operation: ").split()

if sec_arg == "+":
    print(int(first_arg) + int(third_arg))
elif sec_arg == "-":
    print(int(first_arg) - int(third_arg))
elif sec_arg == "*":
    print(int(first_arg) * int(third_arg))
elif sec_arg == "/":
    print(int(first_arg) / int(third_arg))
elif sec_arg == "%":
    print(int(first_arg) % int(third_arf))
else:
    print("Enter input using format: 5 + 2")
