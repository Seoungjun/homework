# print(min(2, 3, 4))
# print(max(2, -3, 4, 7, -5))
# print(max(2, -3, min(4, 7), -5))

# def get_abs(x, y):
#     return abs(x - y)

# def three_times(x):
#     return x * 3

# print(get_abs(-2, 8))
# print(three_times(2))

# def km_to_mile(x):
#     return x / 1.6

# km = float(input("키로미터 입력>"))
# mile = km_to_mile(km)
# print(km, "킬로미터는", mile, "마일 입니다")

def get_average_of_three(a, b, c):
    return (a + b + c) / 3

num1 = int(input("첫번째 정수 점수 입력>"))
num2 = int(input("두번째 정수 점수 입력>"))
num3 = int(input("세번째 정수 점수 입력>"))

avg = get_average_of_three(num1, num2, num3)
print("세 점수의 평균 :", avg)

num4 = int(input("네번째 정수 점수 입력>"))
min_score = min(num1, num2, num3, num4)

if min_score == num1:
    avg = get_average_of_three(num2, num3, num4)
elif min_score == num2:
    avg = get_average_of_three(num1, num3, num4)
elif min_score == num3:
    avg = get_average_of_three(num1, num2, num4)
else:
    avg = get_average_of_three(num1, num2, num3)

print("상위 세 점수의 평균 :", avg)