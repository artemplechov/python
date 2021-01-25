print('Задание: Реализовать структуру "Товары"')

count = int(input("Сколько у Вас товаров? "))
my_list = []
name = 'название:'
price = 'цена:'
quantity = 'количество:'
unit = 'ед.:'

goods = {}

for i in range(count):
    goods[name] = input("название:")
    goods[price] = int(input("цена:"))
    goods[quantity] = int(input("количество:"))
    goods[unit] = input("ед.:")
    my_list.append((i+1,goods))
    goods = {}


result_dict = {}

print(f"Товары {my_list}")

for i in my_list:
    tmp_dict = i[1]
    tmp_name = tmp_dict.get(name)
    tmp_price = tmp_dict.get(price)
    tmp_quantity = tmp_dict.get(quantity)
    tmp_unit = tmp_dict.get(unit)

    if name in result_dict.keys():
        already_found_name = result_dict.get(name)
        already_found_name.append(tmp_name)
        result_dict[name] = already_found_name
    else:
        result_dict[name] = [tmp_name]

    if price in result_dict.keys():
        already_found_price = result_dict.get(price)
        already_found_price.append(tmp_price)
        result_dict[price] = already_found_price
    else:
        result_dict[price] = [tmp_price]

    if quantity in result_dict.keys():
        already_found_quantity = result_dict.get(quantity)
        already_found_quantity.append(tmp_quantity)
        result_dict[quantity] = already_found_quantity
    else:
        result_dict[quantity] = [tmp_quantity]

    if unit in result_dict.keys():
        already_found_unit = result_dict.get(unit)
        already_found_unit.append(tmp_unit)
        result_dict[unit] = already_found_unit
    else:
        result_dict[unit] = [tmp_unit]

print(f"Итоговый словарь {result_dict}")

