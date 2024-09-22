class Transaction:
    def __init__(self,amount,date):
        self.amount = amount
        self.date = date
        self.description = None

    def __str__(self):
        transaction_info = f"Transaction of {self.amount}, on date {self.date}"
        return transaction_info

class Expense(Transaction):
    def __init__(self, category):
        super().__init__(amount, date)
        self.category = category

    def __str__(self):
        transaction_info = "Income " + super().__str__()        
        transaction_info += f", from source {self.source}"

        return transaction_info
        
class Income(Transaction):
    def __init__(self, amount, date, source):
        super().__init__(amount, date)
        self.source = source

    def __str__(self):
        transaction_info = "Income " + super().__str__()        
        transaction_info += f", from source {self.source}"

        return transaction_info

date_in1 = "06-08-24"
source_in1 = "father"
in1 = Income(50, date_in1, source_in1)
print(in1)
