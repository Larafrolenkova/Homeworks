# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1 -> 'One'
# switch_it_up(3 -> 'Three'
# switch_it_up(10000 -> None
# Использовать условный оператор if-elif-else нельзя!

number = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']

def switch_it_up(n):
    if n<0 or n>9:
        return 'None'
    else:
        return number[n]

print('Введите число')
num = input()
if len(num)!=0:
    num = int(num)
    print(num,'=>',switch_it_up(num)) 
else:
    print("Вы ввели пустую строку!")
          