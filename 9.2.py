def decimal_to_binary(n):
    if n == 0:
        return ''
    else:
        return decimal_to_binary(n // 2) + str(n % 2)
num = int(input("Enter a positive integer: "))
if num > 0:
    binary = decimal_to_binary(num)
    print("Binary equivalent:", binary)
elif num == 0:
    print("Binary equivalent: 0")
else:
    print("Please enter a positive integer.")
