def f(subjects):
    average = {}
    for key,value in subjects.items():
        sum=0
        for i in value:
            sum += i
        avg=round(sum/len(value),2)
        average[key] = avg
    highest = max(average.values())
    for key, value in average.items():
        if value!=highest:
            continue
        else:
            return key

print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))
