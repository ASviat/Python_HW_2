# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] - список на основе n, а позиции элементов lst2=[3,1].

length = int(input('Введите количество элементов в списке: '))
list1=[]
import random

for i in range(length):
    list1.append(random.randint(-length,length))
    
print(list1)

positioning1=int(input('Введите первую позицию: '))
positioning2=int(input('Введите вторую позицию: '))
positioning1-=1
positioning2-=1

list2=[positioning1,positioning2]

print(f'Сумма введенных элементов = {list1[positioning1]*list1[positioning2]}')