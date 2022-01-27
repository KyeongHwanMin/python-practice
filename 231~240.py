# 231 코드 결과 예상
# def n_plus_1 (n) :
#     result = n + 1

# n_plus_1(3)
# print (result) # 함수 내부에서 사용한 변수를 외부에서 접근 불가

# def n_plus_1(n):
#     result = n+1
#     return result


# result = n_plus_1(3)
# print(result)

# 232 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수 정의
# def make_url(S):
#     return (f"www.{S}.com")

# print(make_url('naver'))

# 233 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수 정의
# def make_list(String):
#     list = []
#     for s in String:
#         list.append(s)
#     return list

# def make_list2(String):
#    return list(string) # 형변환

# print(make_list("abcd"))

# 235 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수로 정의
# def convert_int(String):
#     return int(String.replace(",", ''))

# print(convert_int("1,234"))

# 236 실행결과 예측
# def 함수(num):
#     return num + 4


# a = 함수(10)
# b = 함수(a)
# c = 함수(b)

# print(c)

# 237 실행결과 예측
# def 함수(num):
#     return num + 4

# c = 함수(함수(함수(10)))
# print(c)

# 238 실행결과 예측
# def 함수1(num):
#     return num + 4


# def 함수2(num):
#     return num * 10


# a = 함수1(10)
# c = 함수2(a)

# print(c)

# 239
# def 함수1(num):
#     return num + 4


# def 함수2(num):
#     num = num + 2
#     return 함수1(num)


# c = 함수2(10)
# print(c)

# 240
# def 함수0(num):
#     return num * 2


# def 함수1(num):
#     return 함수0(num + 2)


# def 함수2(num):
#     num = num + 10
#     return 함수1(num)


# c = 함수2(2)
# print(c)
