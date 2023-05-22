from datetime import datetime

class FinancialRecord:
    def __init__(self, date=None):
        self.date = date or datetime.now().strftime("%Y-%m-%d")
        self.expenses = []
        self.income = []

    def add_expense(self, amount, category):
        expense = {"amount": amount, "category": category}
        self.expenses.append(expense)

    def add_income(self, amount, source):
        income = {"amount": amount, "source": source}
        self.income.append(income)


class Budget(FinancialRecord):
    def __init__(self, limit, date=None):
        super().__init__(date)
        self.limit = limit

    def check_budget(self):
        total_expenses = sum(expense["amount"] for expense in self.expenses)
        if total_expenses > self.limit:
            return "Budget exceeded!"
        else:
            return "Budget is within limit."


class SavingsGoal(FinancialRecord):
    def __init__(self, goal_amount, date=None):
        super().__init__(date)
        self.goal_amount = goal_amount

    def check_goal_progress(self):
        total_income = sum(income["amount"] for income in self.income)
        if total_income >= self.goal_amount:
            return "Savings goal achieved!"
        else:
            return "Keep saving."
