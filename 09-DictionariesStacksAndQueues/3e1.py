import queue
numbers = queue.LifoQueue()

numbers.put(2)
numbers.put(3)
numbers.put(7)
numbers.put(4)
numbers.put(1)
numbers.put(9)
numbers.put(8)

a = numbers.get()
b = numbers.get()
sum_last_two = a+b
print(f'Sum of the last two numbers: {sum_last_two}')
total = 0
while not numbers.empty():
    total+=numbers.get()
print(f'Sum of the remaining numbers: {total}')

