tank_capacity = 255
waterQuantity = 0

n = int(input())

for i in range(n):
    liters = int(input())

    newWaterQuantity = waterQuantity + liters

    if newWaterQuantity > tank_capacity:
        print('Insufficient capacity!')

    else:
        waterQuantity = newWaterQuantity

print(waterQuantity)
