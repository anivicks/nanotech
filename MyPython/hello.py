# num1, num2 = int(input("Enter first number: ")), int(input("Enter second number: "))

# if num1 < num2:
#     print('Second number is greater')
# else:
#     print('First is greater')

# a = ["Pop", "Nitro", "Vicks", "Bezop"]

# for i in range(len(a)):
#     print(i+1, a[i], end="...")

# print(list(range(5)))

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
        
ask_ok('Do you really want to quit?')