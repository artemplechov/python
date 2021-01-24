print('Задание: Реализовать структуру "Товары"')

count = int(input("Сколько у Вас товаров? "))
my_list = []
name = ''
price = 0
quantity = 0
unit = ''
goods = {}

for i in range(count):
    goods["название"] = input("название:")
    goods["цена"] = int(input("цена:"))
    goods["количество"] = int(input("количество:"))
    goods["ед."] = input("ед.:")
   # my_list.append((i+1,goods))
    my_list.append(goods)

#goods["название"] = input("название:")
#goods["цена"] = int(input("цена:"))
#goods["количество"] = int(input("количество:"))
#goods["ед."] = input("ед.:")

print(my_list[1])
#print(goods)

for tmp in my_list:
    print(tmp)

result_dict = {}

#for name in goods.keys():
   # print(name)
   # result_dict['название'].append(name)
   # print(result_dict)
