# -*- coding: utf-8 -*-
import sys
from zxcvbn import password_strength as zxcvbn_password_strength


def enable_win_unicode_console():
    """
    Включаем правильное отображение unicode в консоли под MS Windows
    """
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()


def password_strength(password: str) -> int:
    """
    Вычисляем стойкость пароля
    :param password: текстовый пароль
    :return: стойкость пароля в баллах от 1 до 10
    """
    # список баллов нужен из-за того, что функция от zxcvbn возвращает
    # стойкость пароля в баллах от 0 до 4, а нам нужно от 1 до 10
    password_scores = [1, 3, 5, 7, 10]
    return password_scores[zxcvbn_password_strength(password)['score']]


def print_password_strength_attributes(password: str):
    """
    Печатаем параметры пароля - энтропия, время взлома
    :param password: текстовый пароль
    """
    password_strength_attributes = zxcvbn_password_strength(password)
    print('Энтропия пароля, бит: %s' % password_strength_attributes['entropy'])
    print('Ожидаемое время взлома, сек: %s (%s)' %
          (password_strength_attributes['crack_time'],
           password_strength_attributes['crack_time_display'])
          )


if __name__ == '__main__':

    enable_win_unicode_console()
    user_password = input('Введите пароль для проверки: ').strip()
    print_password_strength_attributes(user_password)
    print('Стойкость пароля по шкале от 1 до 10: %s' %
          password_strength(user_password))
