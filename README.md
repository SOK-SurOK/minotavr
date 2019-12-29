# Минотаврное задание студтрека

Установка pipenv (это виртуальная среда pip):

    sudo apt install pipenv  # для debian-подобных операционных систем
    pip install pipenv  # или через pip
    pip3 install pipenv  # или через pip3

Скачиваем архив  
...  
Переходим в директорию проекта  
...  
И устанавливаем зависимости (прописаны в Pipfile):

    pipenv install

Запускаем скрипт:

    pipenv shell  # Активируем виртуальное окружение
    python cybermans_PSU.py имя_файла_с_массивом
    exit  # Выход из pipenv

Или так запускаем (также из директории проекта):

    pipenv run python cybermans_PSU.py имя_файла_с_массивом


## Внимание:
1. Файл с массивом должен быть такого вида (arr.txt или arr2.txt):
    1. размерность n*n
    2. строки массива разделяются переносом строки
    3. столбцы не разделяются (arr.txt), но если флаг -v2 то столбцы разделяются знаком пробела (arr2.txt)
    4. в последней строке нет лишних знаков (переносов строк, пробелов, табуляции)
    5. 0-проход 1-стена 2-робот
    6. должно быть два робота
