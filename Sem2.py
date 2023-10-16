##Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
##Функцию hex используйте для проверки своего результата.


HEX_FACTOR = 16
hex_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']


def get_number_from_user() -> int:
    enter = input('Введите число > 0: ')
    return int(enter)


def converter(number: int) -> str:
    res: str = ''
    while number > 0:
        res = str(hex_data[number % HEX_FACTOR]) + res
        number //= HEX_FACTOR
    return res


num = get_number_from_user()
if isinstance(num, int):
    print(converter(num))
else:
    print('Что-то не так, попробовать снова')

print(hex(num)[2:])





##Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
##Программа должна возвращать сумму и произведение* дробей. 
##Для проверки своего кода используйте модуль fractions



def process_fractions(frac1_str, frac2_str):
# Преобразуем дроби из строк в числа
    num1, denom1 = map(int, frac1_str.split("/"))
    num2, denom2 = map(int, frac2_str.split("/"))

# Сумма дробей
    sum_frac_num = num1 * denom2 + num2 * denom1
    sum_frac_denom = denom1 * denom2
    sum_frac = (sum_frac_num, sum_frac_denom)

# Произведение дробей
    prod_frac_num = num1 * num2
    prod_frac_denom = denom1 * denom2
    prod_frac = (prod_frac_num, prod_frac_denom)

    return sum_frac, prod_frac

# Использования функции
frac1_str = "3/4"
frac2_str = "2/3"

sum_frac, prod_frac = process_fractions(frac1_str, frac2_str)

print(f"Сумма дробей {frac1_str} и {frac2_str} - {sum_frac[0]}/{sum_frac[1]}")
print(f"Произведение дробей {frac1_str} и {frac2_str} - {prod_frac[0]}/{prod_frac[1]}")
