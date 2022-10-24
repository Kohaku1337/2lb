height = int(input("-| Напишите ваш рост(м): "))
mass = int(input("-| Напишите ваш вес(кг): "))
steps = int(input("-| Сколько шагов вы сегодня прошли: "))
active_time = int(input("-| Сколько заняла времени тренировка(мин): "))


def countTrainingCost(M, H, S, T):
    distance = S * (H / 4 + 0.37)
    speed = int(distance / T)
    energy = int(0.035 * M + (speed ** 2 / H) * 0.029 * M)

    if distance <= 2000:
        motivate_text = ' Зачем ты вышел из дома тренироваться? '
    elif distance <= 4000:
        motivate_text = ' Твой дом все дальше от тебя... '
    elif distance > 4000:
        motivate_text = ' Умоляю вернись домой, тебе спорт не нужен! '

    return distance, energy, motivate_text


print(f"Дистанция(м) - калории:{countTrainingCost(mass, height, steps, active_time)}")
