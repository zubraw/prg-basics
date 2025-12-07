def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print(f'Car Fuel Consumption: {car_fuel_consumption}')
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)
print(f'Sorted Car Fuel Consumption: {sorted_car_fuel_consumption}')
print(f'Bank Transactions: {bank_transactions}')
sorted_bank_transacrions = bubble_sort(bank_transactions)
print(f'Sorted Bank Transactions: {sorted_bank_transacrions}')