#cm = (feet × 30.48) + (inches × 2.54).
#1 stopa  = 12 cali 
# 1 cal  = 2,54 centymetra 
def f(cm):
    inches = cm/2.54
    feet = inches/12
    feet = str(feet)
    print(f'I am {cm}cm tall, i.e. {feet[0]} feet and {feet[2]} inches')
f(175)
    