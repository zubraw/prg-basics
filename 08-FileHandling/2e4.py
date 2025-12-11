employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

job_title ='Software Engineer'

with open(employees_file,'r') as rfile:
    content = rfile.read()
    splitedcontent = content.splitlines()
    with open(position_file,'w') as wfile:
        for line in splitedcontent:
            if job_title in line:
                wfile.write(f'{line}\n')