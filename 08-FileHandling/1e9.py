def reading_from_file(name):
    with open(name) as file:
        content = file.read()
    return content

file_content = reading_from_file('it_company.csv')

job_title = 'Software Engineer'

for line in file_content.splitlines():
    if job_title in line:
        print(line)