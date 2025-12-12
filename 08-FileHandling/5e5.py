import re
#From: Jan Kowalski <jan.kowalski@example.com>
#To: Anna Nowak <anna.nowak@example.com>
#Subject: Report request
with open('email.txt','r') as file:
    content = file.read()

def email_sender():
    sender_pattern = r'^From:.*<([A-Za-z0-9._%+-]+@[A-Za-z0-9._%+-]+\.[A-Za-z]{2,})>$'
    email_match = re.search(sender_pattern, content, re.MULTILINE)
    if email_match:
        return email_match.group(1)
def email_recipient():
    recipient_pattern = r'^To:.*<([A-Za-z0-9._%+-]+@[A-Za-z0-9._%+-]+\.[A-Za-z]{2,})>$'
    email_match = re.search(recipient_pattern, content, re.MULTILINE)
    if email_match:
        return email_match.group(1)

def email_subject():
    subject_pattern = r'^Subject:\s*(.+)$'
    subject_match = re.search(subject_pattern, content, re.MULTILINE)
    if subject_match:
        return subject_match.group(1)

def email_body():
    body_pattern = r'^Hi Anna,\s*[\s\S]+[\d\s]{9,}$'
    body_match = re.search(body_pattern, content, re.MULTILINE)
    if body_match:
        return body_match.group(1).strip()
    

print(email_sender())
print(email_recipient())
print(email_subject())
print(email_body())

#DO POPRAWY