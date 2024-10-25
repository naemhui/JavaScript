numbers = [1, 2, 3]


def square(num):
    return num**2

# map 함수의 특징: 첫 번째 인자로 함수를 받음
new_numbers = list(map(square, numbers))
print(new_numbers)  # [1, 4, 9]
