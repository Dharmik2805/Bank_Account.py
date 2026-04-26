
# ------------------- BANK ACCOUNT CLASS -------------------

class BankAccount:
    """Base class for bank accounts."""
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance  # Encapsulated attribute

    # ---------------- METHODS ----------------
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{self.account_holder} deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"{self.account_holder} withdrew ${amount}. New balance: ${self.__balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"{self.account_holder}'s balance: ${self.__balance}")

    # Encapsulation getter
    def get_balance(self):
        return self.__balance

# ------------------- SAVINGS ACCOUNT SUBCLASS -------------------

class SavingsAccount(BankAccount):
    """Savings account with interest."""
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.04):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    # Method overriding
    def check_balance(self):
        print(f"Savings Account Balance for {self.account_holder}: ${self.get_balance():.2f}")

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest:.2f} added to {self.account_holder}'s account.")

# ------------------- CURRENT ACCOUNT SUBCLASS -------------------

class CurrentAccount(BankAccount):
    """Current account with overdraft."""
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=300):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    # Overriding withdraw method
    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            new_balance = self.get_balance() - amount
            self._BankAccount__balance = new_balance  # Allow negative balance
            print(f"{self.account_holder} withdrew ${amount}. New balance: ${self.get_balance():.2f}")
        else:
            print("Exceeded overdraft limit!")

# ------------------- SIMULATE BANK OPERATIONS -------------------

if __name__ == "__main__":
    print("Bank Account Simulation (Friend's Version)\n")

    # Create multiple objects
    acc1 = SavingsAccount("S2001", "Rohit", 1500)
    acc2 = CurrentAccount("C2002", "Meera", 800)

    # Simulate operations
    acc1.check_balance()
    acc1.deposit(400)
    acc1.withdraw(300)
    acc1.add_interest()
    acc1.check_balance()

    print("\n---\n")

    acc2.check_balance()
    acc2.deposit(200)
    acc2.withdraw(900)  # Uses overdraft
    acc2.withdraw(200)  # Exceeds overdraft
    acc2.check_balance()