import random


def reverse(num):
    """
    :param num:
    :return: reversed num
    """

    reversed_num = 0
    while num != 0:
        reversed_num += (num % 10) * (10 ** (len(str(num)) - 1))
        num //= 10
    return reversed_num


def tuple_to_int(data: tuple):
    """
    :param data: tuple
    :return: data joined like a int number
    """

    number = 0
    times = len(data) - 1
    for i in data:
        number += i * 10 ** times
        times -= 1
    return number


def sum_of_min_max(data):
    """
    :param data:
    :return: sum max and min elements of data
    """
    return min(data) + max(data)


def is_even(num):
    """
    :param num:
    :return: is number True or False
    """
    return num % 2 == 0


def indexes_of_even_elements(data):
    """
    :param data:
    prints indexes of data's even elements
    """
    for i in range(len(data)):
        if is_even(data[i]):
            print(i)


def reversed_word(word):
    """
    :param word:
    :return: reversed word
    """
    res_lst = []
    index = len(word) - 1
    while index > -1:
        res_lst.append(word[index])
        index -= 1
    return "".join(res_lst)


def is_prime(num):
    """
    :param num:
    :return: is num prime or not
    """
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def smallest_prime(n):
    """
    :param n:
    :return: returns smallest prime number after n
    """

    num = n + 1
    while not is_prime(num):
        num += 1
    else:
        return f"The smallest prime number after number {n} is {num}"


def get_median(data):
    """
    :param data:
    :return: median number of data
    """

    if len(data) % 2 != 0:
        return data[len(data) // 2]
    else:
        return (data[len(data) // 2 - 1] + data[len(data) // 2]) / 2


def is_leap(year):
    """
    :param year:
    :return: is year leap or not
    """
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True


def days_month(year, month):
    """
    :param year:
    :param month:
    :return: How many days has the month
    """

    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        if is_leap(year):
            return 29
        return 28
    else:
        return "Wrong data"


def random_passwd(n):

    """

    :param n:
    :return: random password with length n
    """

    pwd_lst = []
    lst = [i for i in range(33, 127)]
    for i in range(n):
        char = random.choice(lst)
        pwd_lst.append(chr(char))
    return "".join(pwd_lst)


def same_parity(n, *args):

    """
    :param n:
    :param args:
    :return: list of arguments, that divided by n
    """

    lst = [each for each in args if each % n == 0]
    return lst

