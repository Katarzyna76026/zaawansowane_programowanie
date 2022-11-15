from zad1 import Student

class Library:
    def __init__(self, city, street, zip_code, open_hours:str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
       return f'Biblioteka w {self.city} na ulicy {self.street}. ' \
               f'Jest otwarta w godzinach {self.open_hours}, tel. do biblioteki to: {self.phone}.'

class Employee:
    def __init__(self, first_name,last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
       return f'Pracownik {self.first_name} {self.last_name}.'

class Book(Library):
    def __init__(self, library: Library, publicatoin_date,author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publicatoin_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Książka autorstwa {self.author_name} {self.author_surname}, wydana w {self.publication_date}.' \
               f'Posiada {self.number_of_pages} stron, znajduje sie w {self.library}.'

class Order(Book):
    def __init__(self, employee, student,books: Book, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Wypożyczenia dokonał student {self.student}, Wypożyczył: {self.employee} ' \
               f'. Wypożyczono dnia {self.order_date} książki: {self.books}.'

slaska = Library('Katowice', 'Rady Europy', '40-021','10.00-18.00',432198765)
sum = Library('Katowice', 'Warszawska', '40-006','7.30-19.30',332293765)

potop = Book(slaska, 1886, 'Henryk', 'Sienkiewicz', 315)
krzyzacy = Book(slaska, 1900, 'Henryk', 'Sienkiewicz', 1215)
panTadeusz = Book(slaska, 1834, 'Adam', 'Mickiewicz', 275)
dziady = Book(sum, 1822, 'Adam', 'Mickiewicz', 50)
zemsta = Book(sum, 1834, 'Aleksander', 'Fredro', 149)

kowalski = Employee('Adam','Kowalski', 2006, 1960, 'Katowice', 'Adamskiego', '42-650', 123456789)
nowak = Employee('Jakub','Nowak', 2004, 1965, 'Katowice', '1 Maja', '22-750', 123456729)
polok = Employee('Ewa','Polok', 2020, 1980, 'Katowice', 'Chorzowska', '45-320', 323456789)

polak = Student('Marcel',[5,5,5])
kowalik = Student('Julia',[3,4,3,4,5])
baran = Student('Pawel',[5,5,4,5])

order1 = Order(kowalski,kowalik,[potop.__str__(),krzyzacy.__str__()], 2022)
order2 = Order(nowak,polak,[zemsta.__str__()], 2022)

print(order1)
print(order2)