gb.ru/lessons/451458 семинары
gb.ru/lessons/407765 лекции

# chance20240712 Lecture1
После создания python -m venv venv
# - для Windows;
# python3 -m venv venv - для Linux и MacOS
не активировалось виртуальное окружение по команде venv\Scripts\activate
# - для Windows;
# source venv/bin/activate - для Linux и MacOS
Проблема исчезла после команды pip# Get-Command java | Select-Object -ExpandProperty Version

# https://winitpro.ru/index.php/2020/06/03/powershell-execution-policy-zapusk-scriptov/
Текущее значение политики выполнения скриптов PowerShell на компьютере можно получить командой: Get-ExecutionPolicy. Если ответ Restricted
Сначала поменять администратора на текущего пользователя командой Set-ExecutionPolicy -Scope CurrentUser
затем Set-ExecutionPolicy RemoteSigned

-m venv - это:
-m - это команда вызова модуля
первый venv - это название модуля

Интерпретаторы python:
CPython
PyPy
StacklessPython
Jython
IronPython

создаем новый проект - это mkdir, синоним создания папки

deactivate - команда завершения работы внутри виртуального окружения

Прежде чем устанавливать дополнения с помощью системы управления пакетами pip (Package Installer for Python) убедитесь, что
находитесь в каталоге проекта и активировали виртуальное окружение.
pip install requests - скачает и установит библиотеку requests (позволяет делать http-запросы) последней версии в папку venv виртуального окружения

команда pip freeze - Убедиться, что установка прошла успешно

pip freeze > requirements.txt (сохраняет все данные, что мы установили)

more requirements.txt - заглянуть в содержимое файла requirements

pip install -r requirements.txt - быстрая установка в новое окружение всего содержимого файла

# Lecture2
Линтер - программа, которая проверяет код

Из модуля typing можно импортировать различные типы данных

sys.getsizeof()
object.__sizeof__()

dir(math.gcd)   # greatest common divisor - наибольший общий делитель
math        # nan - not a number    tau     inf - infinity
decimal     # высокая точность Decimal
fractions   # дроби Fraction
