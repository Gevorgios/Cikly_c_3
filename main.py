# x = int(input("Введите целое число x: "))
# y = int(input("Введите целое число y: "))
#
# result = x ** y
#
# print(f"Значение {x} в степени {y} равно: {result}")

# count = 0
#
# for num in range(100, 1000):
#     digits = [int(digit) for digit in str(num)]
#
#     if len(set(digits)) < len(digits):
#         count += 1
#
# print(f"Количество чисел с двумя одинаковыми цифрами: {count}")


# count = 0
#
# for num in range(100, 10000):
#     digits = [int(digit) for digit in str(num)]
#
#     if len(set(digits)) == len(digits):
#         count += 1
#
# print(f"Количество чисел, у которых все цифры разные: {count}")


# num = int(input("Введите целое число: "))  # Пользовательский ввод
#
# # Преобразуем число в строку, удаляем цифры 3 и 6, а затем преобразуем обратно в число
# new_num = int(str(num).replace("3", "").replace("6", ""))
#
# print(f"Число без цифр 3 и 6: {new_num}")