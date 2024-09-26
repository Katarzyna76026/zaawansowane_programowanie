class Student:
    def __init__(self, name, marks:list) -> bool:
        self.name = name
        self.marks = marks

    def __str__(self):
       return f'Strudent {self.name} oceny: {self.marks}.'

    def is_passed(self):
        suma = 0
        i = 0
        for x in self.marks:
            suma += x
            i += 1

        if(suma/i) > 50:
            print(True)
        else:
            print(False)



jan = Student("Jan", [1,2,3])
jan.is_passed()

ewa = Student("Ewa",[100])
ewa.is_passed()