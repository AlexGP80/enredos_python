class Category:

    def __init__(self, name):
        self.balance = 0
        self.ledger = list()
        self.name = name

    def get_name(self):
        return self.name

    def deposit(self, amount, description=""):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.get_name()}"):
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        return True

    def __str__(self):
        output = ""

        output = f"{self.name:*^30}\n"
        for item in self.ledger:
            output += f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n"
        output += f"Total: {self.balance:.2f}"
        return output

    def __descr__(self):
        return str(self)





def create_spend_chart(categories):
    output = "Percentage spent by category\n"
    total_expenses = 0
    cat_names = []
    cat_expenses = []
    cat_percentages = []
    percentages = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
    longest_name_len = 0

    for category in categories:
        category_expense = 0
        cat_names.append(category.name)
        cat_percentages.append(0)
        for entry in category.ledger:
            amount = entry["amount"]
            if amount < 0:
                total_expenses -= amount
                category_expense -= amount
        cat_expenses.append(category_expense)

    for i in range(len(cat_names)):
        cat_percentages[i] = 10 * int(10 * cat_expenses[i] / total_expenses)
        if len(cat_names[i]) > longest_name_len:
            longest_name_len = len(cat_names[i])

    for percentage in percentages:
        output += f"{percentage:>3}| "
        for cat_percentage in cat_percentages:
            if cat_percentage >= percentage:
                output += "o  "
            else:
                output += "   "
        output += "\n"

    output += "    " + "---"*len(cat_names) + "-"

    for i in range(longest_name_len):
        output += "\n    "
        for name in cat_names:
            if len(name) <= i:
                output += "   "
            else:
                output += f" {name[i]} "
        output += " "

    return output
