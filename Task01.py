# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#    Пример:

# - 6782 -> 23
# - 0,56 -> 11

number = float(input("Введите число: "))



def CountNumbers(num):
    sum = 0
    n=1
    
   
    for i in range (len(str(num))):
        sum+=num[i]
        #sum+=int(num/n%10)
        #n*=10
      
    return sum



print(CountNumbers(number))
