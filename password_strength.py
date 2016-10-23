# -*- coding: utf-8 -*-
import re
import requests
from requests import ConnectionError, HTTPError, Timeout, TooManyRedirects
from zxcvbn import password_strength as zxcvbn_password_strength

PASSWORD_BLACKLIST_FILE_URL = \
    'https://raw.githubusercontent.com/danielmiessler/SecLists/master' + \
    '/Passwords/10_million_password_list_top_1000000.txt'
REQUEST_TIMEOUT = 9  # ожидаем ответ сервера 9 секунд, для плохих соединений
PASSWORD_LENGTH = 8

VULNERABILITIES_INFO = {
    'small_length': 'Длина пароля менее %i' % PASSWORD_LENGTH,
    'no_digits': 'В пароле нет чисел',
    'no_upper_case': 'В пароле нет заглавных букв',
    'no_lower_case': 'В пароле нет строчных букв',
    'no_both_upper_and_lower_case': 'В пароле нет одновременно строчных и ' +
                                    'заглавных букв',
    'no_symbols': 'В пароле нет символов',
    'blacklisted': 'Пароль есть в черном списке %s' %
                      PASSWORD_BLACKLIST_FILE_URL
}


def load_password_blacklist_file_from_url(url: str) -> list:
    """
    Загружаем плохие пароли в виде текста с сервера
    :param url: список с паролями
    :return:
    """
    response = requests.get(url, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.content.decode('utf-8').split('\n')


def get_vulnerabilities(password: str, password_blacklist: str) -> dict:
    vulnerabilities = []
    if len(password) < PASSWORD_LENGTH:
        vulnerabilities.append('small_length')
    if re.search(r'\d+', password) is None:
        vulnerabilities.append('no_digits')
    if re.search(r'[A-Z]', password) is None:
        vulnerabilities.append('no_upper_case')
        no_upper_case = True
    else:
        no_upper_case = False
    if re.search(r'[a-z]', password) is None:
        vulnerabilities.append('no_lower_case')
        no_lower_case = True
    else:
        no_lower_case = False
    if no_upper_case or no_lower_case:
        vulnerabilities.append('no_both_upper_and_lower_case')
    if re.search(r'\W', password) is None:
        vulnerabilities.append('no_symbols')
    is_blacklisted = True if password in password_blacklist else False
    if is_blacklisted:
        vulnerabilities.append('blacklisted')
    return vulnerabilities


def password_strength(password: str):
    """
    Вычисляем стойкость пароля. Подразумевается. что используются только буквы
    латинского алфавита, цифры и символы
    :param password:
    :return:
    """
    password_strength_count = 10


def print_vulnerabilities(vulnerabilities):
    if vulnerabilities:
        for vulnerability in vulnerabilities:
            print(VULNERABILITIES_INFO[vulnerability])
    else:
        print('Уязвимостей не найдено')


if __name__ == '__main__':

    user_password = input('Введите пароль для проверки: ').strip()

    try:
        loaded_password_blacklist = load_password_blacklist_file_from_url(
            PASSWORD_BLACKLIST_FILE_URL
        )
    except ConnectionError:
        print('Ошибка сетевого соединения')
        exit(1)
    except HTTPError:
        print('Сервер вернул неудачный код статуса ответа')
        exit(1)
    except Timeout:
        print('Вышло время ожидания ответа от сервера')
        exit(1)
    except TooManyRedirects:
        print('Слишком много редиректов')
        exit(1)

    found_vulnerabilities = get_vulnerabilities(user_password,
                                                loaded_password_blacklist)
    print_vulnerabilities(found_vulnerabilities)
    zxcvbn_test_results = zxcvbn_password_strength()
