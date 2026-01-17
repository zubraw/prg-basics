class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        fage = int(self.age)
        first_letter = self.name[0]
        #fseniority = str(self.seniority)
        if fage>= 18:
            return f'{self.surname.upper()}{first_letter.upper()}{self.seniority}'
            #result = self.surname.upper() + self.name[0].upper() + fseniority
        elif 0<=fage<18:
            return f'{self.surname.lower()}{first_letter.lower()}{self.seniority}'
            #result = self.surname.lower() + self.name[0].lower() + fseniority
        #return result

print(C("Anna","May",17,7))
print(C("George", "Brown", 21, 4))