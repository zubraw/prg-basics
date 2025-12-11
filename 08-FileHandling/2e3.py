original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

with open(original_file,'r') as file:
    content = file.read()
splied_content = content.splitlines()

with open(target_file,'w') as tfile:
    for line in sorted_content:
        tfile.write(f'{line}\n')