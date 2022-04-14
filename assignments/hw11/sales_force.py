"""
Name: <Jalena Austin>
<Sales Force>.py

Problem: <Creating a class that encapsulates data from another class titled SalesPerson
    to retrieve information from a defined file and order amount of sales people into a specified
    order.>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: <Brook Duvall>
"""
from sales_person import SalesPerson


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        f_name = open(file_name, 'r')
        for lines_r in f_name.readlines():
            lines_r = lines_r.split(',')
            person = SalesPerson(int(lines_r[0]), lines_r[1].strip())
            sales_ord = lines_r[2].split()
            for sale in sales_ord:
                person.enter_sale(float(sale))
            self.sales_people.append(person)
        f_name.close()

    def quota_report(self, quota):
        quota_list = []
        for person in self.sales_people:
            part_list = []
            person_id = person.get_id()
            person_name = person.get_name()
            person_total = person.total_sales()
            if person_total >= quota:
                person_report = True
            else:
                person_report = False
            part_list.append(person_id)
            part_list.append(person_name)
            part_list.append(person_total)
            part_list.append(person_report)
            quota_list.append(part_list)
        return quota_list

    def top_seller(self):
        top_sell_list = []
        sale_leader = self.sales_people[0]
        max_sale = 0

        for i in range(len(self.sales_people)):
            if self.sales_people[i].compare_to(sale_leader) == 1:
                max_sale = self.sales_people[i].total_sales()

        for j in range(len(self.sales_people)):
            if self.sales_people[j].total_sales() == max_sale:
                top_sell_list.append(self.sales_people[j])

        return top_sell_list

    def individual_sales(self, employee_id):
        for i in range(len(self.sales_people)):
            if employee_id == self.sales_people[i].get_id():
                return self.sales_people[i]
        return None

    def get_sale_frequencies(self):
        freq_list = {}
        for person in self.sales_people:
            sale_amt = person.get_sales()
            for sale in sale_amt:
                if freq_list.get(sale, 0) == 0:
                    freq_list[sale] = 1
                else:
                    freq_list[sale] += 1
        return freq_list
