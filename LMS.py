class Student():
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def describe_student(self):
        print('Student Name: ' + self.name + ', Major: ' + self.major + '.')


class Book():
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.description = ('Book Name: ' + self.name + ' Author: ' + self.author)

    def describe_book(self):
        print(self.description)


class LMS():
    def __init__(self):
        self.available_books = []
        self.checked_out_books = []

    def available(self, book):
        self.available_books.append('Book name: ' + book)

    def borrow_books(self, student):
        for book in self.available_books:
            print('Making sure book is available...')
            if book in self.checked_out_books:
                print(book + ' is already checked out by ' + student + ', please wait until it is returned.')
            else:
                self.available_books.remove(book)
                self.checked_out_books.append(book)
                self.checked_out_books.append('Checked out by: ' + student)
                print(self.available_books, self.checked_out_books)

    def return_books(self, student):
        for book in self.checked_out_books:
            self.checked_out_books.remove(book)
            self.checked_out_books.remove('Checked out by: ' + student)
            self.available_books.append(book)
            print('Your book has been returned!')
            print(self.available_books, self.checked_out_books)


Harry_Potter = Book('Harry Potter', 'JK Rowling')
Cool_Robot = Book('Cool Robot', 'Billy Jenkins')
Maze_Runner = Book('Maze Runner', 'James Dashner')

Vedant = Student('Vedant', 'English')
Bob = Student('Bob', 'Math')
Jenna = Student('Jenna', 'Science')

lms1 = LMS()
lms2 = LMS()
lms3 = LMS()

lms1.available(Harry_Potter.name)
lms2.available(Maze_Runner.name)
lms3.available(Cool_Robot.name)

lms1.borrow_books(Vedant.name)
lms2.borrow_books(Jenna.name)
lms1.return_books(Vedant.name)
lms2.return_books(Jenna.name)


