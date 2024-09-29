def calculator():
    num1 = float(input("첫 번째 숫자: "))
    op = input("연산자(+, -, *, /): ")
    num2 = float(input("두 번째 숫자: "))
    
    if op == '+':
        print(f"결과: {num1 + num2}")
    elif op == '-':
        print(f"결과: {num1 - num2}")
    elif op == '*':
        print(f"결과: {num1 * num2}")
    elif op == '/':
        if num2 != 0:
            print(f"결과: {num1 / num2}")
        else:
            print("0으로 나눌 수 없습니다.")
    else:
        print("잘못된 연산자입니다.")
    
calculator()
print("lets go ddc")