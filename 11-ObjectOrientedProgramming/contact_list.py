from contact import Contact

class Contact_list:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact_obj):
        self.contacts.append(contact_obj)
    
    def display(self):
        if not self.contacts:
            print('The contacts list is empty')
        else:
            print('CONTACT LIST')
            print('===================='*3)
            for element in self.contacts:
                print(f'{element.name:20}{element.email:20}{element.telephone:20}')
