# Создайте модуль module_4_1 (если ещё не создан), импортируйте в него функции divide из модулей fake_math и true_math,
# назвав их разными именами на своё усмотрение, чтобы не было конфликтов имён, при помощи оператора as.
# Запустите эти функции в модуле module_4_1, передав первым аргументом произвольное число отличное от 0,
# вторым аргументом - 0
# Выведи результаты вызовов этих функций на экран(в консоль).

from fake_math import divide as f_d
from true_math import divide as t_d

result1 = f_d(69, 3)
result2 = f_d(3, 0)
result3 = t_d(49, 7)
result4 = t_d(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)



