height = int(input("-| Напишите ваш рост(м): "))
mass = int(input("-| Напишите ваш вес(кг): "))
steps = int(input("-| Сколько шагов вы сегодня прошли: "))
active_time = int(input("-| Сколько заняла времени тренировка(мин): "))


def countTrainingCost(M, H, S, T):
    distance = S * (H / 4 + 0.37)
    speed = int(distance / T)
    energy = int(0.035 * M + (speed ** 2 / H) * 0.029 * M)

    if distance <= 2000:
        motivate_text = ' Ты прошел неплохую дистанцию! '
    elif distance <= 4000:
        motivate_text = ' Твои достижения в прохождении шагов стали еще выше... '
    elif distance > 4000:
        motivate_text = ' Твой результат достиг максимума, поздравляю! Фраз на большие дистанции больше не будет( : '

    return distance, energy, motivate_text


print(f"Дистанция(м) - калории:{countTrainingCost(mass, height, steps, active_time)}")
