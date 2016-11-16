# -*- coding: utf-8 -*-
from getpass import getpass
import sys
from zxcvbn import password_strength


def get_password_strength(password: str) -> int:
    """
    Вычисляем стойкость пароля
    :param password: текстовый пароль
    :return: стойкость пароля в баллах от 1 до 10
    """
    score = password_strength(password)['score']
    return (score + 1) * 2 if score != 0 else 1


def print_password_strength_attributes(password: str):
    """
    Печатаем параметры пароля - энтропия, время взлома
    :param password: текстовый пароль
    """
    password_strength_attributes = password_strength(password)
    print('Энтропия пароля, бит: %s' % password_strength_attributes['entropy'])
    print('Ожидаемое время взлома, сек: %s (%s)' %
          (password_strength_attributes['crack_time'],
           password_strength_attributes['crack_time_display'])
          )
    print('Стойкость пароля по шкале от 1 до 10: %s' %
          get_password_strength(password))


if __name__ == '__main__':

    user_password = getpass('Введите пароль для проверки: ').strip()
    print_password_strength_attributes(user_password)

