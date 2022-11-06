"""Игра в угадай число. Компьютер загадывает и угадывает"""
import numpy as np

def random_predict(number:int=1) -> int:
    """_summary_

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1,100) # предполагаемое число
        if number == predict_number:
            break
        
    return count


def score_game(random_predict) -> int:
    """за какое количество в среднем за 1000 угадывает

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: количество попыток
    """
    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size = (100)) 
    
    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f'Score = {score}')    

if __name__ == '__main__':
    score_game(random_predict)