import json

# Read the contents of the json file
with open('voting.json','r') as file:
    content = file.read()
    votes = json.loads(content)


# Vote for a person
person_name = input('Name of the person you are voting for:')
if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1
print(votes)

 # Save voting data to json file
with open('voting.json','w') as file:
    json.dump(votes, file, indent=4)
