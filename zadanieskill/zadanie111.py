import json

with open('../orders_2023.json', 'r') as file:
    data = json.load(file)
#print(data['o_182356']['price'])

max_price = 0
max_price_order_number = ''

for order_num, orders_data in data.items():
    price = orders_data['price']

    if price > max_price:
        max_price_order_number = order_num
        max_price = price

print(f'Номер самого дорогого заказа за июль: {max_price_order_number}')

max_quantity = 0
max_date = ''
max_quantity_order_number = ''
max_user = 0

for order_num, orders_data in data.items():
    quantity = orders_data['quantity']
    date = orders_data['date']
    user_id = orders_data['user_id']

    if quantity > max_quantity:
        max_quantity_order_number = order_num
        max_quantity = quantity
        max_date = date
        max_user = user_id

print(f'номер заказа с самым большим количеством товаров: {max_quantity_order_number}')
print(f'больше всего заказов было сделано в день: {max_date}')
print(f'самое большое количество заказов за июль сделал пользователь: {max_user}')
print(f'пользователь у которого самая большая суммарная стоимость заказов за июль: {max_user}')

total_price = sum(item['price'] for item in data.values())
average_price = total_price / len(data)

print(f"средняя стоимость заказа была в июле: {average_price}")
print(f"средняя стоимость товаров в июле: {average_price}")









