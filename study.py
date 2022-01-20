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


class Store:
    def __init__(self, jjajang, jjampong):
        self.jjajang = jjajang 
        self.jjampong = jjampong

    def total_order(self):
        return (self.jjajang + self.jjampong)

    @classmethod 
    def same4each(cls):
        print("dddddd")

    @staticmethod
    def nameofstore():
        print("북경반점")

Order = Store(3,2)
Order.same4each()