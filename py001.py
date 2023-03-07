print('При покупке четырёх и более билетов Вам будет предоставлена скидка 10%!')
a = 1
while a:
    Tickets_str = input("Введите количество билетов: ")
    if not Tickets_str:
        continue
    else:
        Tickets = int(Tickets_str)
        if Tickets == 1 or Tickets % 10 == 1 and Tickets != 11:
            print('Вы хотите приобрести', Tickets, 'билет.')
            a -= 1
        elif Tickets in [2,3,4] or Tickets % 10 in [2,3,4] and Tickets not in [12, 13, 14]:
            print('Вы хотите приобрести', Tickets, 'билета.')
            a -= 1
        elif 5 <= Tickets < 100 and Tickets % 10 not in [2,3,4] or Tickets in [12, 13, 14]:
            print('Вы хотите приобрести', Tickets, 'билетов.')
            a -= 1
        else:
            print('Введите число больше 0 и меньше 100.')
if Tickets > 3:
    print('Вам будет предоставлена скидка 10%!')
print('---------------')
print("""Стоимость билетов:\n
      1) детям до 18 лет вход бесплатный.\n
      2) от 18 до 25 лет: 990 руб.\n
      3) старше 25 лет: 1390 руб.\n""")
print('---------------')
result_sum = 0
Ticket_cost = None
Age = None
Client_number = 1
Tickets_1 = Tickets
while Tickets_1:
    Age = int(input("Введите возраст "+str(Client_number)+"го посетителя: "))
    if 0 < Age < 18:
            print('Стоимость', str(Client_number),'го билета: бесплатно.')
            Ticket_cost = 0
            Tickets_1 -= 1
            Client_number += 1
            result_sum += Ticket_cost
    elif 18 <= Age < 25:
            print('Стоимость', str(Client_number),'го билета: 990 руб.')
            Ticket_cost = 990
            Tickets_1 -= 1
            Client_number += 1
            result_sum += Ticket_cost
    elif 25 <= Age < 100:
            print('Стоимость', str(Client_number),'го билета: 1390 руб.')
            Ticket_cost = 1390
            Tickets_1 -= 1
            Client_number += 1
            result_sum += Ticket_cost
    else:
             print("Введите возраст от 0 до 100 лет")
else:
    print('---------------')
    if Tickets > 3:
        print('Общая сумма к оплате, с учетом скидки 10%:', result_sum * 0.9, 'руб.')
    else:
        print('Общая сумма к оплате:', result_sum, 'руб.')