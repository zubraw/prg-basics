class Ebook:
    def __init__(self, title, author, num_of_pages):
        self.title = title
        self.author = author
        self.num_of_pages = num_of_pages
        self.current_page_num = 1
        self.open = False
    
    def open_book(self):
        self.open = True
    
    def close_book(self):
        self.open = False

    def next_page(self):
        if self.open and self.current_page_num<self.num_of_pages:
            self.current_page_num+=1
    
    def show_status(self):
        if self.open:
            return f'Title {self.title}, author: {self.author}\n Number of pages: {self.num_of_pages} (current page: {self.current_page_num})\n Book is opened'
        else:
            return f'Title {self.title}, author: {self.author}\n Number of pages: {self.num_of_pages} (current page: {self.current_page_num})\n Book is closed'


def main():
    my_book = Ebook('Harry Potter: Zakon Feniksa', 'J.K. Rowling', 960)
    print(my_book.show_status())
    my_book.open_book()
    print(my_book.show_status())
    my_book.next_page()
    my_book.next_page()
    my_book.next_page()
    print(my_book.show_status())
    my_book.close_book()
    print(my_book.show_status())
    my_book.next_page()
    print(my_book.show_status())
if __name__ == '__main__':
    main()