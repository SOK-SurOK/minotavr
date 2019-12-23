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
    python cybermans_PSU.py
    exit  # Выход из pipenv

Или так запускаем (также из директории проекта):

    pipenv run python cybermans_PSU.py



## Внимание:
 1. Лабиринты изначально должны быть представимы как сетка 17на17, а не как 
 17на18(p1.jpg) или 16на17(p2.jpg)
