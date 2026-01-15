import json
def f(years, course, average_grade):
    with open('data.json','r',encoding='utf-8') as file:
        content = json.load(file)
        counter=0
        for student in content:
            if student['age'] < years:
                continue
            for courses in student['studies']['courses']:
                if courses['name'] == course:
                    avg = sum(courses['grades'])/len(courses['grades'])
                    if avg >= average_grade:
                        counter+=1
                    break
    return counter
print(f(21, "statistics", 4))

