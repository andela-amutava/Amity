class Person(object):
    def __init__(self, name, employee_type, need_accomodation="N"):
        self.id = id(self)
        self.name = name
        self.employee_type = employee_type
        self.need_accomodation = need_accomodation


class Fellow(Person):
    def __init__(self, name, employee_type, accomodation):
        super(Fellow, self).__init__(
            name, employee_type="fellow", need_accomodation="N")


class Staff(Person):
    def __init__(self, name, employee_type="Staff", accomodation="N"):
        super(Staff, self).__init__(name, employee_type, need_accomodation="N")