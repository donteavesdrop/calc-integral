import math
import numpy as np
def f(x):
    return x ** 3 + 1
def CALC_Integral(a, b, num_experiments):
    random_x = np.random.uniform(a, b, num_experiments)
    random_y = np.random.uniform(0, max(f(random_x)), num_experiments)
    #подсчет количества точек, которые находятся под кривой функции на интервале [a, b]
    points_under_curve = sum(random_y <= f(random_x))
    integral = (points_under_curve / num_experiments) * (b - a) * max(f(random_x))
    return integral


# Заданные параметры для интеграла
a = 0
b = 2

# Список чисел экспериментов
num_experiments = [10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7]

# Точное значение интеграла (можно вычислить аналитически)
integral_end = (b ** 4 + 4) / 4

# Создаем вектора для хранения результатов серий
seria_1 = [CALC_Integral(a,b,n) for n in num_experiments]
seria_2 = [CALC_Integral(a,b,n) for n in num_experiments]
seria_3 = [CALC_Integral(a,b,n) for n in num_experiments]
#Раcсчитываем погрешность
#Cредний результат по пяти сериям для каждого из соответствующего числа экспериментов
eps1 = [abs((pi - integral_end)/integral_end) for pi in seria_1]
eps2 = [abs((pi - integral_end)/integral_end) for pi in seria_2]
eps3 = [abs((pi - integral_end)/integral_end) for pi in seria_3]
#Погрешность вычислений для усредненных значений
eps = [(a1+a2+a3)/5 for a1, a2, a3 in zip(seria_1, seria_2, seria_3)]
eps_end = [abs((s-integral_end)/integral_end) for s in eps]
# Выводим результаты
print(f"Cерия 1, Оценка интеграла: {seria_1}\n Погрешность: {eps1}")
print(f"Cерия 2, Оценка интеграла: {seria_2}\n Погрешность: {eps1}")
print(f"Cерия 3, Оценка интеграла: {seria_3}\n Погрешность: {eps1}\n")
print(f"Погрешность вычислений для усредненных значений: {eps_end}")

