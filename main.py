# The entry point of you application

from data.data import resources, FORMAT

'''
    A welcome message to welcome the user 
    A user_choice method that requests the user to input their choice of either to print or run printer maintainers or generate report.
    The off method carries out the printer maintainers by turning it off
'''

welcome = "\nWelcome to Xpress Automated Printing Services\nWhat would you like to do today?\n"

print(welcome)

class Printer:
    # Adds a class object attribute
    coloured_print = FORMAT['coloured']['price']
    greyscale_print = FORMAT['greyscale']['price']
    
    def __init__(self, user_prompt):
        self.user_prompt = user_prompt
       
    def user_choice(self):
        self.user_prompt = input("\nPlease enter 'print' to print or 'off' to run maintainers or 'report' to generate report: \n")

        while self.user_prompt not in ['print','off','report']:
            self.user_prompt = input("Wrong format!!! \nPlease enter 'print' to print or 'off' to run maintainers or 'report' to generate report: \n")
        
        if self.user_prompt == "print" :
            self.user_prompt = input("\nEnter 'coloured' to print in coloured or 'greyscale' to print in greyscale: \n")
            
            if self.user_prompt == "coloured":
                print(f"\nThe price for coloured printing is #{Printer.coloured_print} per page")

            elif self.user_prompt == "greyscale" :
                print(f"\nThe price for greyscale printing is #{Printer.greyscale_print} per page")    
    
    def run_maintainers(self) :
        while self.user_prompt == "off" :
            print("Thank you for using our services")
            exit()

'''
    The Costing class inherits the Printer class methods and has it's own methods that generates reort and verify resources 
'''
class Costing(Printer) :

    # Adds a class object attribute
    ink_resource = resources["ink"]
    paper_resource = resources["paper"]
    profit = resources["profit"]

    def __init__(self, number_of_pages = 0, ink_required = 1):
        super().__init__(user_prompt= '')
        self.number_of_pages = number_of_pages
        self.ink_required = ink_required 

    def generate_report(self) :
        
        if self.user_prompt == "report":
            
            print(f"\nink: {Costing.ink_resource}ml\npaper: {Costing.paper_resource}pc\nprofit: #{Costing.profit}")
            self.user_prompt = input("\nEnter 'print' to print or 'off' to run maintainers or 'report' to generate report: \n")
            
            while self.user_prompt not in ['print','off','report']:
                self.user_prompt = input("Wrong format!!! \nPlease enter 'print' to print or 'off' to run maintainers or 'report' to generate report: \n")
        
        if self.user_prompt == "print" :
            self.user_prompt = input("\nEnter 'coloured' to print in coloured or 'greyscale' to print in greyscale: \n")
        
            if self.user_prompt == "coloured":
                print(f"The price for coloured printing is #{Printer.coloured_print} per page")

            elif self.user_prompt == "greyscale" :
                print(f"The price for greyscale printing is #{Printer.greyscale_print} per page")    
            
        Printer.run_maintainers(self)
        
    
    def verify_resource(self):
        while True:
            try:
                self.number_of_pages = int(input("\nPlease enter the number of pages you want to print: "))

                if self.user_prompt == "coloured":
                    ink_per_page = 7
                    self.ink_required = ink_per_page * self.number_of_pages
                elif self.user_prompt == "greyscale" :
                    ink_per_page = 5 
                    self.ink_required = ink_per_page * self.number_of_pages
                break
            except ValueError:
                print("\nInvalid number of pages. Please enter the number of pages you would like to print")

    def check_further(self):

        while self.number_of_pages > self.paper_resource or self.ink_required > self.ink_resource:
            print("\nNot enough paper or ink")
            Costing.verify_resource(self)

'''
    The ProcessCost class inherits the Costing class and by default inherits the Printer class. 
'''   

class ProcessCost(Costing):

    def __init__(self, deposit = 0):
        super().__init__(number_of_pages= 0, ink_required=1)
        self.deposit = deposit 

    def amount(self, price = 0):
        one_coloured_page = FORMAT['coloured']['price']
        one_greyscale_page = FORMAT['greyscale']['price']

        Printer.user_choice(self)
        Costing.generate_report(self)
        Costing.verify_resource(self)
        Costing.check_further(self)

        if self.user_prompt == "coloured":
            self.price = one_coloured_page * self.number_of_pages
            print(f"\nYour fee is #{self.price}")
        elif self.user_prompt == "greyscale":
            self.price = one_greyscale_page * self.number_of_pages
            print(f"\nYour fee is #{self.price}")
    
    def check_currency(self):
        print("\nPlease insert currency")
        while True:
            try:

                biyar = int(input("\nPlease enter the number of Biyar: ")) * 5
                faiba = int(input("\nPlease enter the number of Fibar: ")) * 10
                muri = int(input("\nPlease enter the number of Muri: ")) * 20
                wazobia = int(input("\nPlease enter the number of Wazobia: ")) * 50
                self.deposit = biyar + faiba + muri + wazobia
                break
            
            except ValueError:
                print("\nCurrency should be in an integer format!!!")
            
        if self.price > self.deposit :
            print("\nSorry that’s not enough money. Money refunded")

        elif self.price < self.deposit :
            balance_left = self.deposit - self.price 
            print(f"\nHere is your #{balance_left} balance")
            print("\nHere is your Project. Thank you for using our services")
        else:
            print("Here is your Project. Thank you for using our services")

    def report_update(self):
        
        while self.price < self.deposit or self.price == self.deposit:
            Printer.user_choice(self)
            Costing.ink_resource = Costing.ink_resource - self.ink_required
            Costing.paper_resource = Costing.paper_resource - self.number_of_pages
            Costing.profit = Costing.profit + self.price

            if self.user_prompt == "report":
                print(f"ink: {Costing.ink_resource}ml\npaper: {Costing.paper_resource}pc\nprofit: #{Costing.profit}")
            break
            

def to_be_used_again():
    Costing()
    checker = ProcessCost()
    checker.amount()
    checker.check_currency()
    checker.report_update()

while True:
    to_be_used_again()







