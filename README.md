# Решение задачи [№6](https://devman.org/challenges/6/) с сайта [devman.org](https://devman.org)

## Условие задачи:

Вот выдержка из статьи на Википедии про правильные пароли:

1) Использование строчных и заглавных букв
2) Использование чисел
3) Использование специальных символов, таких как @, #, $
4) Запрет на использование слов, найденных в черных списках паролей
5) Запрет слов, найденных в информации о пользователе
6) Запрет использования имени компании
7) Запрет паролей, содержащих календарные даты, 
8) Запрет паролей, содержащих номера лицензий, 
9) Запрет паролей, содержащих телефонные номера, 
10) Запрет часто встречающихся номеров.

В этой задаче требуется написать скрипт, который просит ввести пароль и 
выдаёт ему оценку от 1 до 10. 
1 – очень слабый пароль, 10 – очень крутой.
## Системные требования

```
Python 3.5.2+
Внешний модуль win-unicode-console
Внешний модуль zxcvbn (с GitHub, так как тот, что в pip - не работает)
```

## Установка

Windows

```    
git clone https://github.com/ram0973/6_password_strength.git
cd 6_password_strength
pip install -r requirements.txt
```

Linux
```    
git clone https://github.com/ram0973/6_password_strength.git
cd 6_password_strength
pip3 install -r requirements.txt
```
    
## Описание работы
```
Пользователь вводит пароль с клавиатуры.
Стойкость пароля считаем, как указано здесь:
https://blogs.dropbox.com/tech/2012/04/zxcvbn-realistic-password-strength-estimation/
Скрипт выводит оценку от 1 до 10. 
1 – очень слабый пароль, 10 – очень сильный. 
```
    
## Запуск

Windows

python password_strength.py
 
Linux
 
python3 password_strength.py

## Лицензия

[MIT](http://opensource.org/licenses/MIT)