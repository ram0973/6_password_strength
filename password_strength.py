# -*- coding: utf-8 -*-
from getpass import getpass
from zxcvbn import password_strength


def get_password_strength(password):
    return [1, 3, 5, 7, 10][password_strength(password)['score']]

if __name__ == '__main__':
    print('Password strength from 1 to 10: %s' %
          get_password_strength(getpass('Input password: ').strip()))
