from zad1 import Student

class Library:
    def __init__(self, city, street, zip_code, open_hours:str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
       return('Biblioteka w miescie: ' + self.city + ' na ulicy: '+ self.street + ' kod pocztowy: ' + self.zip_code + '. Godziny otwarcia: ' + self.open_hours + ' telefon:' + self.phone) 

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
       return('Nazwisko: ' + self.first_name + ' Imie: '+ self.last_name + ' data zatrudnienia: ' + self.hire_date + ' data urodzenia ' + self.birth_date + ' miasto: ' + self.city + ' ulica '+ self.street + ' kod pocztowy: ' + self.zip_code + ' telefon: ' + self.phone) 

class Book(Library):
    def __init__(self, library:Library, publicatoin_date,author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publicatoin_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return('Biblioteka ' + self.library + ' data publikacji ' + self.publication_date + ' autor ' + self.author_name + ' ' + self.author_surname + 'liczba stron' + self.number_of_pages)

class Order(Book):
    def __init__(self, employee, student,books: list (Book), order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return('dane pracownika: ' + self.employee + ' dane studenta: ' + self.student + ' wypożyczone książki: ' + self.books + ' data zamówienia: ' + self.order_date)

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