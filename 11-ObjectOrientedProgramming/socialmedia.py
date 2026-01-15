class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        i = 1
        for post in self.posts:
            print(f'{i}. {self.username}: {post}')
            i += 1
    

def main():
    user1 = SocialMediaProfile('johndoe')
    user1.add_post('Hello, world!')
    user1.add_post('Had a great day at the park!')
    user1.add_post('Whats up, Natalie? How are you?')
    user1.display_timeline()

    user2 = SocialMediaProfile('zubraw')
    user2.add_post('Japierdole samych debili mi daje na te flexy')
    user2.add_post('Kurwa adc mają teraz dodatkowego slota na itemy??')
    user2.add_post('XDDDDD kurwa tahm kench full build zostaje oneshotowany przez caitlyn')
    user2.add_post('Pierdole tą gre pobieram dote')
    user2.display_timeline()

if __name__ == "__main__":
    main()