class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def display_info(self):
        return (f'Title: {self.title}, Author: {self.author}, Year: {self.year}') 
    
    
title = input('enter title of this book:')
author = input('enter author of this book:')
while True:
        year = input('enter year of publishing of this book:')
        try:
            year_int = int(year)
            if 1000 <= year_int <= 2025:
                break
            else:
                print('Please enter a valid year between 1000 and 2025.')
        except ValueError:
            print('Please enter a valid integer for the year.')
year = str(year_int)
book1 = Book(title, author, year)
print(book1.display_info())        
