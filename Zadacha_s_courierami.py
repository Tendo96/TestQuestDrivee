import math

def distance(coord1, coord2):
    
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def assign_orders(orders, couriers):
    assignments = {}
    for order in orders:
        min_distance = float('inf')
        assigned_courier = None
        for courier in couriers:
            d = distance(order['A'], courier)
            if d < min_distance:
                min_distance = d
                assigned_courier = courier
        if assigned_courier not in assignments:
            assignments[assigned_courier] = []
        assignments[assigned_courier].append(order)
    return assignments

orders = [
    {'A': (62.027751, 129.731413), 'B':(62.029605, 129.763489), 'cost': 350},
    {'A': (1, 1), 'B':(5, 15), 'cost': 250},
    {'A': (0.111, 1.4), 'B':(0.23, 3.45), 'cost': 300},
]

couriers = [(62.026884, 129.728718), (3, 4), (0.23, 0.423)]

assignments = assign_orders(orders, couriers)
for courier, assigned_orders in assignments.items():
    print(f"Для курьера с координатами {courier} назначены заказы:")
    for order in assigned_orders:
        print(f"Заказ из точки {order['A']} в {order['B']} стоимостью {order['cost']}")
