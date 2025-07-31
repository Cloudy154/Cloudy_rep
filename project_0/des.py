import numpy as np
number = np.random.randint(1, 101)# загадываем число
print(number)
count = 0
while True:
    count += 1
    predict_number = int(input("Введите число от 1 до 100:"))
    if predict_number > number:
        print("Ваше число больше!")
    elif predict_number < number:
        print("Ваше число меньше!")
    else:
        print(f"Верно! Попыток затрачено {count}")
        break
    
def my_func (n):
    pass
            