# def test_generator():
# 		yield 1
# 		yield 2
# 		yield 3

# gen = test_generator()
# print(type(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# # print(next(gen))

# for i in test_generator():
# 	print(i)

# def add(*args):
# 	result = 0
# 	for i in args:
# 		result += i
# 	print(result)

# add(1,10,100)

# def name_and_age(**kwargs):
# 	print(kwargs)

# name_and_age("민경환","35")

# def number_and_name(*args, **kwargs):
# 	print(args,kwargs)

# number_and_name(1,2,name="민경환")

# def add(f_arg, *args):
# 	print("첫 번재 인자", f_arg)
# 	for arg in args:
# 		print("args의 다른 인자", arg)

# add("처음",1,2,3)

# def name_and_age(**kwargs):
# 	print(kwargs)

# name_and_age(name="민경환",age="35")

# def greet_me(**kwargs):
#     if kwargs is not None:
#         for key, value in kwargs.items(): # python3: 
#             print(f'{key}-{value}')

# greet_me(name="민경환", age="35")

# def test_args_kwargs(arg1, arg2, arg3):
# 	print(f"인자1:{arg1}")
# 	print(f"인자2:{arg2}")
# 	print(f"인자3:{arg3}")

# args=("two",3,5)
# test_args_kwargs(*args)

# kwargs = {"arg3":3, "arg2":"two","arg1":5}
# test_args_kwargs(**kwargs)

# class Person:
# 	# class Person의 멤버 변수
# 	name = "민경환"
# 	number = "01011112222"
# 	age = "34"

# 	#class Person의 메소드
# 	def info(self):
# 		print(f"제 이름은 {self.name}입니다.")
# 		print(f"제 번호는 {self.number}입니다.")
# 		print(f"제 나이는 {self.age}입니다.")
	
# #__name__ :interpreter가 실행 전에 만들어 둔 글로벌 변수.
# if __name__ == "__main__": # main namespace를 의미 (인터프리터에서 직접 실행된 경우에만 실행)
# 	customer = Person() 
# 	customer.info()

# class Monster:
#     def __init__(self,hp,atk,dfn):
#         self.hp = hp
#         self.atk = atk
#         self.dfn = dfn
 
#     def attack(self,target):
#         target.ReduceHP(self.atk)
 
#     def ReduceHP(self,atk) :
#         self.hp = self.hp - (atk-self.dfn)
 
# # if __name__ == "__main__":
# m1 = Monster(100,10,3)
# m2 = Monster(100,10,3)
# m1.attack(m2)
# print(m2.hp)

	
# a = 1
# print('a:', id(a))
# a += 1
# print('a+1:', id(a))

# b = 1
# print('b:', id(b))

# c = 2
# print('c:', id(c))

# class Strore:
# 	def __init__(self,jjajang, jjampong):
# 		self.jjajang = jjajang
# 		self.jjampong = jjampong

# 	def total_order(self):
# 		return (self.jjajang + self.jjampong)

# 	@classmethod
# 	def same4each(cls, double):
# 		return cls(double, double)

# Order1 = Strore(3,2)
# print(Order1.total_order())

# Order2 = Strore.same4each(3)
# print(Order2.total_order())

# print(Strore.same4each(10).total_order())

# class Windows:
#     os = "window10"		# 클래스 속성

#     def __init__(self):
#         self.out = "OS: " + self.os
        
#     @staticmethod
#     def static_os():
#         return Windows()

#     @classmethod
#     def class_os(cls):
#         return cls()

#     def os_output(self):
#         print(self.out)

# class Linux(Windows):
#     os = "Linux"		# 클래스 속성

# a = Linux.static_os()
# a.os_output()

# b = Linux.class_os()
# b.os_output()

# c = Windows.class_os()
# c.os_output()


# class Store:
#     def __init__(self, jjajang, jjampong):
#         self.jjajang = jjajang 
#         self.jjampong = jjampong

#     def total_order(self):
#         return (self.jjajang + self.jjampong)

#     @classmethod 
#     def same4each(cls):
#         print("dddddd")

#     @staticmethod
#     def nameofstore():
#         print("북경반점")

# Order = Store(3,2)
# Order.same4each()

# str메서드 : 클래스 자체의 내용을 출력하고 싶을때
# class Blog():
#     def __init__(self, title, date):
#         self.title = title
#         self.date = date
#     def __str__(self):
#         return f"제목:{self.title}, 날짜:{self.date}"

# blog = Blog('파이썬',2022)
# print(blog)


# # or 연산자 1나만 참이면 참
# result1 = 1 or True 
# result2 = False or 1 
# result3 = False or False or 2 
# #and 연산자 둘다 참이여야 참
# result4 = True and False 
# result5 = True and False or 'a' # a 출력
# result6 = 1 != 1 and 2 or 3 # 3 출력
# result7 = 'a' if True else 'b'
# result8 = 'a' if 1 == 2 else 'b'
# reuslt9 = 'a' if 1 == 1 else 'b'
# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)
# print(result6)
# print(result7)
# print(result8)
# print(reuslt9)

#list comprehension
size = 10
arr = [i *2 for i in range(size)]
print(arr)
new_arr = [ n*n for n in arr]
print(new_arr)
word = '가나다'
print([c*2 for c in word]) # 파이썬에서 문자열은 한글자씩 순회 가능
arr = [ i for i in range(1,11) if i % 2 == 0]
print(arr)
arr = [i for i in range(1, 31) if i % 2 == 0 if i % 3 == 0] # 'and' 없이 조건문을 나열하면 AND 조건으로 계산됨. 'and' 명시 해주면 에러뜸
print(arr)
arr = [i for i in range(1,31) if i % 2 == 0 or i % 3==0] # if 문을 1개만 쓰고 'or' 연산자로 논리 연산을 묶어준다.
print(arr)

# ===========================
#set comprehension 기호 {}
set_boy = {n**2 for n in range(10)} 
print(set_boy)
print(set(range(10)))

#dict compreshension 기호 {}
#set 과의 구분  key : value 쌍을 써주고, 사용하는 변수를 두개로 둔다.
from string import ascii_lowercase as LOWERS
dict_boy = { k:v for k, v in zip(LOWERS, range(1,28))}
print(dict_boy)
print(dict(zip(LOWERS, range(1, len(LOWERS)+1))))

#tuple compreshension 기호 () 
tuple_boy = (n for n in range(1,10)) # ()는 제네레이터(순회객체)를 생성하는 generator comprehension이다.
print(tuple_boy)
tuple_boy = tuple(n for n in range(1,10))
print(tuple_boy)
