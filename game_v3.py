"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
import math


def smart_predict(number: int = 1) -> int:
    """Угадываем число, изменяя ответ на все более маленькую величину

    Args:
        number (int, optional):  Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
        
    count = 0
    predict_number = 50
    dif = 25 #Величина изменения
    
    while True:
        count += 1
        if number < predict_number:
            predict_number -= dif
        elif number > predict_number:
            predict_number += dif
        elif number == predict_number:
            break  # выход из цикла если угадали
        dif = math.ceil(dif/2)
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(
        1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(smart_predict)
