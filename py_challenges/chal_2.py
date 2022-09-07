"""
과제 2
사용자에게 두가지 정수를 입력 받고 +, -, *, / 선택한 후 계산 결과를 출력
사용자가 exit를 입력하기 전까지 계속 반복
"""

calculator = True

while calculator:
    choice_num = int(input("Choose a number: "))
    another_num = int(input("Choose another one: "))
    user_operation = input("Choose an operation: \n Options are: +, _, * or /. \n Write 'exit' to finish. \n")
    if user_operation == 'exit':
        calculator = False
        result = 'end'
    elif user_operation == '+':
        result = choice_num + another_num
    elif user_operation == '-':
        result = choice_num - another_num
    elif user_operation == '*':
        result = choice_num * another_num
    else:
        result = choice_num / another_num
    print(f'Result : {user_operation}')