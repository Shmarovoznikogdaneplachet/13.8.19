tickets = int(input('Здравствуйте, сколько билетов Вы хотите приобрести? Введите количество:'))
if tickets > 0:
    L = [i for i in range(tickets)] # список количества билетов
print(L)
print('Вводите возраст посетителя и нажимайте enter:')
print('Для окончания ввода просто нажмите enter:')
a = int(input('-->>'))
vozrast = [] # список возрастов
while True:
    try:
        vozrast.append(a)
        a = int(input('-->>'))
    except:
        break
print(vozrast)

k = 18
h = 25
count = 0
for i in vozrast:
    if 18 <= i < 25:
        count = count + 1
print('Количество посетителей возрастом от 18 до 25 лет:' + str(count))

count2 = 0
for i in vozrast:
    if i >= 25:
        count2 = count2 + 1
print('Количество посетителей возрастом от 25 лет:' + str(count2))

count3 = 0
for i in vozrast:
    if i < 18:
        count3 = count3 + 1
print('Количество посетителей возрастом до 18 лет:' + str(count3))

x = count*990 + count2*1390 + count3*0
print('Общая стоимость билетов составила:', x, 'рублей')

y = count + count2 + count3
print('Всего билетов:', y)
if y > 3:
    x = x*0.1
    print('Вы заказали больше 3 билетов, поздравляем, Ваша скидка составила:', x, 'рублей')