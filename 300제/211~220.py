#211 함수의 호출 결과를 예측하라.
# def 함수(문자열):
#     print(문자열)

# 함수("안녕")
# 함수("Hi")

#212 함수의 호출 결과를 예측하라.
# def 함수(a, b):
#     print(a+b)

# 함수(3,4)
# 함수(7,8)

#213 아래와 같은 에러가 발생하는 원인을 설명하라.
# def 함수(문자열):
#     print(문자열)

# 함수() # 파라미터 값을 정해주지 않아서 에러발생.

#214 아래와 같은 에러가 발생하는 원인을 설명.
# def 함수(a,b):
#     print(a+b)

# 함수("안녕",3) # 파라미터로 받은 문자열과 숫자는 연산이 불가하기 때문에.

#215 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라
# def print_with_smile(string):
#     print(string+":D")
    

#216 215에서 정의한 함수 호출 파라미터는 "안녕하세요"
# print_with_smile("안녕하세요")

#217 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
# def print_upper_price(price):
#     print(price * 1.3)

#218 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수 정의
# def print_sum(a,b):
#     print(a+b)

#219 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.
# def print_arithmetic_operation(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)

# print_arithmetic_operation(3,4)

#220 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max함수를 정의하라. 단 if문을 사용해서 수를 비교하라.
def print_max(a,b,c):
    if a > b & a >c:
        print(a)
    elif b > a & b > c:
        print(b)
    else: print(c) 

print_max(2,3,4)   