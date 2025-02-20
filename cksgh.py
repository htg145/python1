from tkinter.font import names
#
# fruits = ["orange", "apple", "banana"] #리스트
# numbers = [6,3,1,5] #숫자 리스트
# bools = [True, False, True] #불리언 리스트
# mixed_list = ["안녕하세요", 12, True]

# print(fruits[2][1])
# print(fruits[-2])
#
# fruits[1] = "cherry"
# print(fruits)

# numbers.append("hi")
# # print(numbers)
# # numbers.insert(1, 2)
# # print(numbers)
# # numbers.pop()
# # numbers.remove("hi")
# print(numbers)
#
# del numbers[5]
# print(numbers)
#
# print(len(mixed_list)) #리스트 길이

# numbers.sort(reverse=True) #sort()작은순 reverse=True 큰순
# print(numbers)
#
# fruits.sort()
# print(fruits)
#
# bools.sort(reverse=True)
# print(bools)

# numbers.reverse() # 그냥 순서를 거꾸로
# print(numbers)

# fruits = "-".join(fruits)
# print(fruits)

# cart = []
# cart.append(input("추가할 상품 : "))
# cart.append(input("추가할 상품 : "))
# cart.append(input("추가할 상품 : "))
#
# print(cart)

#튜플
colors = ("red", "green", "bleak", "yellow") #변경 불가
numbers = (1, 5, 3, 9, 1, 9)
bools = (True, False, True)
mixed_tuple = ("red", 1, True)

#a = ("first",) #요소가 하나일때는 마지막 쉼표 ! !

print(colors[1])
#colors[1] = "yellow" #튜플 변경 불가능

print(numbers[0:2])
print(numbers.count(1))
print(numbers.index(3))

a, b, c, d = colors
print(c)











































