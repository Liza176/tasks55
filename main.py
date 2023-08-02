# import random

# n = random.randint(1,100)

# print('Я загадал число от 1 до 100')
# for i in range(5):
#     t = int(input())
#     if t > n:
#         print('Число меньше')
#     elif t < n:
#         print('Число больше')
#     else:
#         print('Молодец')

# print('Вы проиграли')

with open (f'a.txt','r',encoding='utf-8') as file:
    count = 0
    count1 = 1
    e1 = file.read()
    mas = ['а','я','у','ю','о','е','ё','э','и','ы']
    mas1 = []

    for u in str(e1):
        if u in mas:
            if u == '\n':
                count1 +=1
                count += 1
                print(count1)
                mas1.append(f'{count1}:{count}')
                
                    

    print(mas1)    
        
