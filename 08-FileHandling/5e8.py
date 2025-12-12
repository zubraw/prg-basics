with open('files.txt','r') as file:
    content = file.read()
content_lines = content.splitlines()
for line in content_lines:
    if len(line)>=5:
        if line[-5]=='.':
            print(line)