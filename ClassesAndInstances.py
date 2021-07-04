class Employee:
    raise_amount : int = 1.04 #class variable, cann be accessed via class or instance
    def __init__(self, firstname, Lastname, pay, email):
        self.first_name = firstname
        self.last_name = Lastname
        self.pay = pay
        self.email = email

    def full_name(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name

    def apply_raise(self):
        pay = int(self.pay * self.raise_amount)
        return pay



e1 = Employee('jonu','chauhan',4000,'jonu.chauhan@gmail.com')
"when we are calling method via instances then we dont need to pass instance"

print(e1.full_name())

"When we are calling method on class then we have to pass instance as self"

print(Employee.full_name(e1))

print(e1.apply_raise())

print(e1.raise_amount)

print(Employee.raise_amount)

print(e1.__dict__)

print(Employee.__dict__)