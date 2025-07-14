# octal to decimal

# def OctalToDecimal(num):
#     decimal_value = 0
#     base = 1

#     while num:
#         last_digit = num % 10
#         num = int(num / 10)
#         decimal_value += last_digit * base
#         base = base * 8
#     return decimal_value

# print("The decimal value of",512, " is",OctalToDecimal(512))

def a(num):
    while num:
        last=num%10
        num=int(num/10)