"""
Name: <Jalena Austin>
<Sales Person>.py

Problem: <Creating a class to encapsulate data from a single sales person.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = int(employee_id)
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(float(sale))

    def total_sales(self):
        return sum(self.sales)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if other.total_sales() > self.total_sales():
            return int(-1)
        elif self.total_sales() > other.total_sales():
            return int(1)
        elif other.total_sales() == self.total_sales():
            return 0

    def __str__(self):
        return "{0}-{1}: {2}".format(self.get_id(), self.get_name(), self.total_sales())
