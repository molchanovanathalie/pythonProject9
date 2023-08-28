# Урок 9. Декораторы
# Основное:
# Создать декоратор для использования кэша. Т.е.
# сохранять аргументы и результаты в словарь,
# если вызывается функция с агрументами, которые уже записаны
# в кэше - вернуть результат из кэша, если нет - выполнить функцию.
# Кэш лучше хранить в json.
# Решение, близкое к решению данной задачи было разобрано на семинаре.
#


import json
from typing import Callable


def json_logging(func: Callable):
    try:
        with open(f'{func.__name__}.json', 'r') as data:
                    result_list = json.load(data)
                    for res_data in result_list:
                        if (res_data['num_input'] == num_input):
                            print(res_data['result'])
                            exit()
    except FileNotFoundError:
        result_list = []


    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result_list.append({'args': args, **kwargs,
                            'num_input': num_input,
                            'result': result
                            })
        with open(f'{func.__name__}.json', 'w') as data:
            json.dump(result_list, data, indent=4)
        return result
    return wrapper


num_input = int(input('введите число ', ))

@json_logging
def guessing(num):
    user_choice = num_input

    if user_choice == num:
        return  True
    elif user_choice < num:
        print('искомое число больше')
    else:
        print('искомое число меньше')
    return  False



if __name__ == "__main__":
    guessing(num = 3)
