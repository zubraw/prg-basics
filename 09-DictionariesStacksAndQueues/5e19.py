import json

def num_of_rooms(res):
    number = 0
    for num in res:
        number+=1
    return number

def paid_reservations(res):
    paid = 0
    for res in res:
        if res['paid']:
            paid+=1
    return paid

def unpaid_reservations(res):
    unpaid = 0
    for res in res:
        if res['paid'] == False:
            unpaid+=1
    return unpaid

def value_paid(res):
    total_paid = 0
    for i in res:
        if i['paid']:
            total_paid+=(int(i['price_per_night']) * int(i['nights']))
    return total_paid

def value_unpaid(res):
    total_unpaid = 0
    for i in res:
        if i['paid'] == False:
            total_unpaid+=(int(i['price_per_night']) * int(i['nights']))
    return total_unpaid

with open('reservations.json','r',encoding='utf-8') as file:
    content = json.load(file)

print('Reservations:', num_of_rooms(content['reservations']))
print(paid_reservations(content['reservations']))
print(unpaid_reservations(content['reservations']))
print(value_paid(content['reservations']))
print(value_unpaid(content['reservations']))