# id, list, set, dict, tuple,  print, zip, all, any, ascii, len, locals, range, max, map, min, next, repr, round, sum, type, hash, dir

#id(object) : 매개변수가 한 개 반드시 있어야함.
# 객체의 'identity'를 반환, 고유하고  일정하게 유지되는 정수, 라이프타임이 겹치지 않으면 두 객체의 id 값이 같을 수 있음.
# 세부정보 : 메모리에 있는 객체의 주소.
# 객체를 입력받아 객체의 고유 주소 값(레퍼런스)를 돌려주는 함수.

# a = 3
# id(3)
# print(id(3))
# print(id(a))
# b = a
# print(id(b))
# 3, a, b가 같은 객체를 가리킴

#####################################################################################################################################################
#class list([iterable]) : 함수라기 보다는, 목록 및 시퀀스(순서) 유형(변경 가능한 mutable)
#iterable : 반복할 수 있는
#반복 가능한 자료형을 입력받아 리스트로 만들어 돌려주는 함수.

# print(list("minkyeonghwan"))
# print(list((1,2,3,4,5)))
# a = ["10","100","1000"]
# b = list(a)
# c = a
# print(b)
# print(c)
# [] 대괄호를 사용하여 빈 목록 표시
# [a],[a,b,c] : 대괄호 사용, 쉼표로 구분
# [x for x in iterable] : list comprehension 사용
# list() or list(iterable) : 생성자 사용

#####################################################################################################################################################
#class set([iterable]) : 집합과 비슷, 순서가 없다, 중복 불가
# test = set([1,2,3,4,5])
# print(test)
# print(type(test))
# test2 = {1,2,3,4,5}
# print(test2)
# print(type(test))
# test2.add(8)
# print(test2)
# test3 = {1,1,2,2,3,3,4,4,5,5}
# print(test3)
# test4 = {c for c in 'abracadabra' if c not in 'abc'} 
# print(test4)
# {'jack','sjoerd'} : 중괄호 안에 쉼표로 구분된 리스트 사용
# {c for c in 'abracadabra' if c not in 'abc'} : set comprehension 사용
# set(), set('foobar'), set(['a','b','c']) : 생성자 사용

#####################################################################################################################################################
# class dict(**kwarg), class dict(mapping, **kwarg), class dict(iterable, **kwarg)
# 사전 클래스
# dictest = {'name':'민경환','phone':'010-5833-3333'}
# print('name' in dictest)
# print('address' in dictest)
# print(dictest.keys())
# print(dictest.values())
# print(dictest.items())
# dictest2 = {x: x ** 2 for x in range(10)}
# print(dictest2)

#{'jack': 4098, 'sjoerd': 4127} : 쉼표로 키, 값 구분
#{x: x **2 for x in range(10)} : dict comprehension
#dict(), dict(['foo', 100), ('bar', 200)]), dict(foo=100, bar=200) : 생성자 사용

#####################################################################################################################################################
#class tuple([iterable]) : 함수라기 보다는 immutable 시퀀스 타입
#tuple(iterable) 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수. 리스트와 같고 특이 점은 값 변경 불가
# t1 = (1,) # 값 1개만 입력받는 방법
# t2 = 1,2,3
# t3 = ('a','b',('ab','cd'))
#() : 괄호를 사용
#a, or (a,) : 싱글톤 튜플에 콤마 사용
# a, b, c or (a, b, c) : 쉼표로 항목 구분
#tuple() or tuple(iterable) : 기본제공 튜플 사용

#####################################################################################################################################################