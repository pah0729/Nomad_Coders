variable = '변수'

my_name = 'Lucy'
age = 26
dead = False

# print(f"Hello my name is {my_name} and I'm {age} years old")


def say_hello(user_name='anonymous', user_age=0):
    print(f'Hello, {user_name} how are you?')
    print(f'you are {user_age} years old')

say_hello('lucy', 26)
print()


def tax_calculator(money):
    print(money * 0.35)

tax_calculator(int(input('숫자를 입력하세요 >> ')))

