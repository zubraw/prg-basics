with open('it_company.csv','r') as file:
    content = file.read()
company = content.splitlines()

n=1
while n < len(company):
    for i in range(5):
        if n < len(company):
            print(company[n])
            n+=1
    input('Press Enter key...')